@echo off
set "SCRIPT_PATH=%~dp0run_bot.bat"
echo Setting up daily task to run: "%SCRIPT_PATH%" at 09:00 AM

schtasks /create /tn "GitHubActivityBot" /tr "\"%SCRIPT_PATH%\"" /sc daily /st 09:00

if %errorlevel% neq 0 (
    echo.
    echo Failed to create task. Please try running this script as Administrator.
    pause
    exit /b %errorlevel%
)

echo.
echo Task "GitHubActivityBot" created successfully!
echo It will run every day at 09:00 AM.
pause
