@echo off
cd /d "%~dp0"
echo Running GitHub Activity Bot...
python activity_bot.py
timeout /t 5
