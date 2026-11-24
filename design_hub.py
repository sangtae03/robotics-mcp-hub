#!/usr/bin/env python3
"""Collect selected upstream robotics repositories without installing or running them."""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CATALOG = ROOT / "design-app-dev.catalog.json"
REPOSITORY_PATTERN = re.compile(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+")


class HubError(Exception):
    pass


def load_catalog(path: Path = CATALOG) -> list[dict]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        raise HubError(f"Cannot read catalog: {exc}") from exc
    if data.get("schema_version") != 1 or not isinstance(data.get("items"), list):
        raise HubError("Unsupported catalog schema.")
    items = data["items"]
    seen_ids: set[str] = set()
    seen_repos: set[str] = set()
    for item in items:
        if not isinstance(item, dict):
            raise HubError("Catalog entries must be objects.")
        repo = item.get("repository", "")
        if not isinstance(repo, str) or REPOSITORY_PATTERN.fullmatch(repo) is None:
            raise HubError("Invalid repository name in catalog.")
        if any(part in {".", ".."} for part in repo.split("/")):
            raise HubError("Invalid repository path.")
        expected_id = repo.lower().replace("/", "--")
        if item.get("id") != expected_id:
            raise HubError(f"Unexpected local folder id: {repo}")
        if item.get("url") != f"https://github.com/{repo}.git":
            raise HubError(f"Only canonical public GitHub clone URLs are accepted: {repo}")
        if expected_id in seen_ids or repo.lower() in seen_repos:
            raise HubError(f"Duplicate catalog entry: {repo}")
        if not isinstance(item.get("category"), str) or not item["category"]:
            raise HubError(f"Missing category: {repo}")
        if not isinstance(item.get("recommended"), bool):
            raise HubError(f"Missing recommendation flag: {repo}")
        seen_ids.add(expected_id)
        seen_repos.add(repo.lower())
    return items


def select_items(items: list[dict], *, all_items=False, recommended=False,
                 categories=None, repos=None, allow_default=False) -> list[dict]:
    categories = categories or []
    repos = repos or []
    available_categories = {c for item in items for c in [item["category"], *item.get("legacy_categories", [])]}
    unknown_categories = set(categories) - available_categories
    if unknown_categories:
        raise HubError("Unknown categories: " + ", ".join(sorted(unknown_categories)))
    aliases = {}
    for item in items:
        aliases[item["id"].lower()] = item["id"]
        aliases[item["repository"].lower()] = item["id"]
    selected_ids = set()
    for value in repos:
        if value.lower() not in aliases:
            raise HubError(f"Unknown repository: {value}; run 'python hub.py list'.")
        selected_ids.add(aliases[value.lower()])
    has_selection = all_items or recommended or categories or repos
    if not has_selection:
        if allow_default:
            return list(items)
        raise HubError("Choose --recommended, --category NAME, --repo OWNER/NAME, or --all.")
    return [
        item for item in items
        if all_items
        or (recommended and item["recommended"])
        or any(c in categories for c in [item["category"], *item.get("legacy_categories", [])])
        or item["id"] in selected_ids
    ]


def git_run(args: list[str], *, timeout=60) -> str:
    env = os.environ.copy()
    env["GIT_TERMINAL_PROMPT"] = "0"
    env["GIT_LFS_SKIP_SMUDGE"] = "1"
    try:
        result = subprocess.run(
            ["git", *args], text=True, encoding="utf-8", errors="replace",
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=timeout, env=env,
        )
    except FileNotFoundError as exc:
        raise HubError("Git is not installed or is not on PATH.") from exc
    except subprocess.TimeoutExpired as exc:
        raise HubError(f"Git command timed out after {timeout}s.") from exc
    if result.returncode:
        detail = result.stderr.strip().splitlines()
        raise HubError(detail[-1] if detail else f"git exited with {result.returncode}")
    return result.stdout.strip()


def comparable_remote(url: str) -> str:
    value = url.rstrip("/")
    return value[:-4] if value.endswith(".git") else value


def existing_checkout(item: dict, destination: Path) -> bool:
    if destination.is_symlink():
        raise HubError(f"Refusing a symbolic-link checkout: {destination}")
    if not destination.exists():
        return False
    if not (destination / ".git").exists():
        raise HubError(f"Folder already exists and is not a Git checkout: {destination}")
    origin = git_run(["-C", str(destination), "config", "--get", "remote.origin.url"])
    if comparable_remote(origin) != comparable_remote(item["url"]):
        raise HubError(f"Folder belongs to a different upstream: {destination}")
    return True


def clone_one(item: dict, dest: Path) -> str:
    destination = dest / item["id"]
    if existing_checkout(item, destination):
        return "skipped"
    dest.mkdir(parents=True, exist_ok=True)
    # Clone into a temporary sibling. Failed clones never occupy the final folder.
    with tempfile.TemporaryDirectory(prefix=".hub-clone-", dir=dest) as temporary:
        staging = Path(temporary) / "checkout"
        git_run(
            ["clone", "--depth", "1", "--no-recurse-submodules", "--",
             item["url"], str(staging)],
            timeout=600,
        )
        if destination.exists() or destination.is_symlink():
            raise HubError(f"Destination appeared while cloning; leaving it untouched: {destination}")
        staging.rename(destination)
    return "downloaded"


def add_selection(parser, *, include_all=True):
    if include_all:
        parser.add_argument("--all", action="store_true", dest="all_items",
                            help="Select all repositories.")
    parser.add_argument("--include-archived", action="store_true", help="Include archived repositories.")
    parser.add_argument("--recommended", action="store_true",
                        help="Select the recommended starting points.")
    parser.add_argument("--category", action="append", default=[],
                        help="Select a category; repeatable.")
    parser.add_argument("--repo", action="append", default=[],
                        help="Select an OWNER/REPO or local id; repeatable.")


def make_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    listing = commands.add_parser("list", help="Show the catalog.")
    add_selection(listing)
    information = commands.add_parser("info", help="Show upstream links and notes.")
    information.add_argument("repository")
    fetching = commands.add_parser("fetch", help="Download selected source checkouts.")
    add_selection(fetching)
    fetching.add_argument("--dest", type=Path, default=ROOT / "design-tools")
    fetching.add_argument("--dry-run", action="store_true", help="Print the plan; write nothing.")
    status = commands.add_parser("status", help="Inspect downloaded checkouts.")
    status.add_argument("--dest", type=Path, default=ROOT / "design-tools")
    commands.add_parser("sectors", help="Show sectors and repository counts.")
    commands.add_parser("doctor", help="Show environment information without changing it.")
    return parser


def main(argv=None) -> int:
    parser = make_parser()
    args = parser.parse_args(argv)
    try:
        items = load_catalog()
        if args.command == "sectors":
            catalog_data = json.loads(CATALOG.read_text(encoding="utf-8"))
            sectors = catalog_data.get("sectors", {})
            for key, label in sectors.items():
                count = sum(item["category"] == key for item in items)
                print(f"{key:14} {count:3}  {label}")
            print(f"\n{len(items)} repositories / {len(sectors)} sectors.")
            return 0

        if args.command == "doctor":
            print("Python:", sys.version.split()[0])
            print("Python executable:", sys.executable)
            print("Platform:", sys.platform)
            print("Git:", git_run(["--version"]) if shutil.which("git") else "not found")
            print("ROS_DISTRO:", os.environ.get("ROS_DISTRO", "(not sourced)"))
            print("Catalog repositories:", len(items))
            print("ROS, Isaac Sim, cameras and motors were not started.")
            return 0

        if args.command == "info":
            matches = select_items(items, repos=[args.repository])
            item = matches[0]
            print(item["title"])
            print("Repository:", item["repository"])
            print("URL:", "https://github.com/" + item["repository"])
            print("README:", item["readme_url"])
            print("Category:", item["category"])
            print("Purpose:", item["description"])
            print("Notes:", item["notes"])
            return 0

        if args.command in {"list", "fetch"}:
            chosen = select_items(
                items, all_items=args.all_items, recommended=args.recommended,
                categories=args.category, repos=args.repo,
                allow_default=args.command == "list",
            )
            if not args.include_archived:
                chosen = [item for item in chosen if not item.get("archived", False)]
            if args.command == "list":
                for item in chosen:
                    mark = "*" if item["recommended"] else " "
                    print(f'{mark} [{item["category"]}] {item["repository"]}')
                    print("    " + item["description"])
                print(f"\n{len(chosen)} repositories. * = recommended starting point")
                return 0
            dest = args.dest.expanduser().resolve()
            if args.dry_run:
                for item in chosen:
                    print(f'{item["url"]} -> {dest / item["id"]}')
                print(f"\nPlan: {len(chosen)} repositories. No files were written.")
                return 0
            if not shutil.which("git"):
                raise HubError("Install Git first, then rerun this command.")
            failures = 0
            for index, item in enumerate(chosen, 1):
                print(f'[{index}/{len(chosen)}] {item["repository"]}', flush=True)
                try:
                    outcome = clone_one(item, dest)
                    print("   " + outcome, flush=True)
                except HubError as exc:
                    failures += 1
                    print("   ERROR: " + str(exc), file=sys.stderr, flush=True)
            print(f"\nFinished: {len(chosen) - failures} downloaded/already present; {failures} failed.")
            print("Open each upstream README for dependency installation and setup.")
            return 1 if failures else 0

        if args.command == "status":
            dest = args.dest.expanduser().resolve()
            errors = 0
            present = 0
            for item in items:
                destination = dest / item["id"]
                if not destination.exists() and not destination.is_symlink():
                    continue
                present += 1
                try:
                    existing_checkout(item, destination)
                    revision = git_run(["-C", str(destination), "rev-parse", "--short=12", "HEAD"])
                    dirty = bool(git_run(["-C", str(destination), "status", "--porcelain"]))
                    print(f'{item["repository"]}: {revision} {"modified" if dirty else "clean"}')
                except HubError as exc:
                    errors += 1
                    print(f'{item["repository"]}: ERROR: {exc}', file=sys.stderr)
            print(f"\n{present} present; {len(items) - present} not downloaded.")
            return 1 if errors else 0
    except HubError as exc:
        print("ERROR: " + str(exc), file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

