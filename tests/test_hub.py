import contextlib
import copy
import io
import json
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

import hub


class CatalogTests(unittest.TestCase):
    def setUp(self):
        self.items = hub.load_catalog()

    def test_all_catalog_sources_and_recommendations(self):
        self.assertEqual(len(self.items), 96)
        self.assertEqual(len({i["repository"] for i in self.items}), 96)
        selected = hub.select_items(self.items, recommended=True)
        self.assertEqual(len(selected), 15)
        self.assertIn("robotmcp/ros-mcp-server", {i["repository"] for i in selected})

    def test_selection_union_deduplicates_and_unknown_fails(self):
        chosen = hub.select_items(self.items, recommended=True,
                                  repos=["Tibe31/so101-mcp"])
        self.assertEqual(len(chosen), 15)
        self.assertEqual(len(hub.select_items(self.items, categories=["so101"])), 12)
        with self.assertRaises(hub.HubError):
            hub.select_items(self.items, repos=["misspelled/source"])
        with self.assertRaises(hub.HubError):
            hub.select_items(self.items)

    def test_catalog_rejects_external_url_and_path_traversal(self):
        for field, value in [("url", "https://example.invalid/code.git"),
                             ("id", "../../outside")]:
            bad = copy.deepcopy(self.items[0])
            bad[field] = value
            with tempfile.TemporaryDirectory() as directory:
                path = Path(directory) / "catalog.json"
                path.write_text(json.dumps({"schema_version": 1, "items": [bad]}))
                with self.assertRaises(hub.HubError):
                    hub.load_catalog(path)

    def test_dry_run_is_complete_and_writes_nothing(self):
        with tempfile.TemporaryDirectory() as directory:
            destination = Path(directory) / "must-not-exist"
            output = io.StringIO()
            with contextlib.redirect_stdout(output):
                code = hub.main(["fetch", "--all", "--dry-run", "--dest", str(destination)])
            self.assertEqual(code, 0)
            self.assertEqual(output.getvalue().count("https://github.com/"), 96)
            self.assertFalse(destination.exists())


@unittest.skipUnless(shutil.which("git"), "Git is required")
class CheckoutTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        self.source = self.root / "upstream"
        self.source.mkdir()
        hub.git_run(["init", str(self.source)])
        hub.git_run(["-C", str(self.source), "config", "user.name", "Hub tests"])
        hub.git_run(["-C", str(self.source), "config", "user.email", "hub-test@example.invalid"])
        (self.source / "README.md").write_text("local upstream\n")
        hub.git_run(["-C", str(self.source), "add", "README.md"])
        hub.git_run(["-C", str(self.source), "commit", "-m", "Initial local fixture"])
        # Local fixtures exercise cloning without making a network request.
        self.item = {"id": "test--upstream", "url": str(self.source),
                     "repository": "test/upstream"}
        self.destination = self.root / "downloads"

    def tearDown(self):
        self.temporary.cleanup()

    def test_clone_and_rerun_preserve_user_edits(self):
        self.assertEqual(hub.clone_one(self.item, self.destination), "downloaded")
        checkout = self.destination / self.item["id"]
        (checkout / "README.md").write_text("my local changes\n")
        self.assertEqual(hub.clone_one(self.item, self.destination), "skipped")
        self.assertEqual((checkout / "README.md").read_text(), "my local changes\n")
        self.assertEqual(hub.git_run(["-C", str(checkout), "rev-parse", "HEAD"]),
                         hub.git_run(["-C", str(self.source), "rev-parse", "HEAD"]))

    def test_unrelated_folder_and_remote_are_never_overwritten(self):
        checkout = self.destination / self.item["id"]
        checkout.mkdir(parents=True)
        (checkout / "keep.txt").write_text("keep me")
        with self.assertRaises(hub.HubError):
            hub.clone_one(self.item, self.destination)
        self.assertEqual((checkout / "keep.txt").read_text(), "keep me")
        hub.git_run(["init", str(checkout)])
        hub.git_run(["-C", str(checkout), "remote", "add", "origin",
                     "https://github.com/another/source.git"])
        with self.assertRaises(hub.HubError):
            hub.clone_one(self.item, self.destination)
        self.assertEqual((checkout / "keep.txt").read_text(), "keep me")

    def test_failed_clone_leaves_no_partial_checkout(self):
        missing = dict(self.item, url=str(self.root / "nonexistent"))
        with self.assertRaises(hub.HubError):
            hub.clone_one(missing, self.destination)
        self.assertFalse((self.destination / self.item["id"]).exists())
        self.assertEqual(list(self.destination.glob(".hub-clone-*")), [])


if __name__ == "__main__":
    unittest.main()

