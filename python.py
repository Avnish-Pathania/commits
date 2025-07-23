import os
import subprocess
from datetime import datetime, timedelta
import random

# Set your name and email (used for commits)
GIT_USER_NAME = "Avnish-Pathania"
GIT_USER_EMAIL = "avnishpathania44@gmail.com"

# How many days back you want to start faking commits
days = 30  # Change this to go further back
max_commits_per_day = 5  # Max commits per day

# Setup user
subprocess.call(["git", "config", "user.name", GIT_USER_NAME])
subprocess.call(["git", "config", "user.email", GIT_USER_EMAIL])

for i in range(days):
    date = datetime.now() - timedelta(days=i)
    num_commits = random.randint(1, max_commits_per_day)
    for j in range(num_commits):
        with open("log.txt", "a") as file:
            file.write(f"Fake commit for {date} #{j}\n")
        subprocess.call(["git", "add", "log.txt"])
        env = os.environ.copy()
        fake_date = date.strftime("%Y-%m-%dT12:00:00")
        env["GIT_COMMITTER_DATE"] = fake_date
        env["GIT_AUTHOR_DATE"] = fake_date
        subprocess.call(["git", "commit", "-m", f"Fake commit {j} on {date.date()}"], env=env)

print("✅ Done faking commits!")

