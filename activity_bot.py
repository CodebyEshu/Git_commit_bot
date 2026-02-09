import os
import subprocess
import datetime
import random

# Configuration
FILE_TO_UPDATE = "daily_log.txt"
COMMIT_MESSAGE_PREFIX = "Daily activity log"
BRANCH_NAME = "main"  # Change to "master" if needed
PROBABILITY = 1.0  # Set to 1.0 for every run, or e.g., 0.5 for 50% chance

def run_git_command(commands):
    try:
        result = subprocess.run(commands, check=True, capture_output=True, text=True)
        print(f"Success: {' '.join(commands)}")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error running: {' '.join(commands)}")
        print(e.stderr)

def main():
    # Randomly decide whether to contribute if probability is < 1.0
    if random.random() > PROBABILITY:
        print("Skipping contribution today based on probability.")
        return

    # specific workspace directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)

    # 1. Update the file
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"Activity logged at: {timestamp}\n"
    
    with open(FILE_TO_UPDATE, "a") as f:
        f.write(log_entry)
    
    print(f"Updated {FILE_TO_UPDATE} with timestamp: {timestamp}")

    # 2. Git commands
    # Check if git checks for changes
    status = subprocess.run(["git", "status"], capture_output=True, text=True)
    if FILE_TO_UPDATE not in status.stdout and "nothing to commit" in status.stdout:
         print("No changes to commit.")
         return

    run_git_command(["git", "add", FILE_TO_UPDATE])
    run_git_command(["git", "commit", "-m", f"{COMMIT_MESSAGE_PREFIX}: {timestamp}"])
    
    # 3. Push
    # Note: This requires credentials to be set up (SSH or Credential Manager)
    run_git_command(["git", "push", "origin", BRANCH_NAME])

if __name__ == "__main__":
    main()
