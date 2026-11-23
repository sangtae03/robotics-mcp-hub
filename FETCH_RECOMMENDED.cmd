@echo off
cd /d "%~dp0"
where py >nul 2>nul
if not errorlevel 1 (
  py -3 hub.py fetch --recommended %*
) else (
  python hub.py fetch --recommended %*
)
if errorlevel 1 (
  echo Download failed. Check the message above.
  pause
  exit /b 1
)
pause

