# GitHub Activity Bot

This tool helps maintain regular activity on your GitHub profile by automatically modifying a file and pushing commits daily (or on alternate days).

## Setup Instructions

1.  **Initialize a Git Repository**:
    Open a terminal in this folder (`C:\Users\LENOVO\.gemini\antigravity\scratch\github_activity_bot`) and run:
    ```cmd
    git init
    # Replace with your GitHub repository URL
    git remote add origin https://github.com/CodebyEshu/Git_commit_bot.git
    echo "# GitHub Activity Bot" > README.md
    git add .
    git commit -m "Initial commit"
    git push -u origin main
    ```

    *Make sure you have SSH keys or Git Credential Manager set up so `git push` works without asking for a password every time.*

2.  **Test the Bot**:
    Double-click `run_bot.bat` to test. A new entry should be added to `daily_log.txt`, and it should simulate a push (if git is configured).

3.  **Schedule Daily Activity**:
    Right-click `setup_task.bat` and select **Run as Administrator**.
    This will create a Windows Task Scheduler job that runs the bot every day at 09:00 AM.

## Configuration

You can open `activity_bot.py` in a text editor to change:
-   `PROBABILITY`: Set to `1.0` (always run) or check logic for random days.
-   `FILE_TO_UPDATE`: The file that gets modified (default: `daily_log.txt`).
-   `BRANCH_NAME`: Default is `main`.

## Disclaimer

Regular commits are great, but genuine contributions are better! Use this responsibly.
