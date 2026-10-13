import datetime
import os
import random
import subprocess

start_date = datetime.date(2024, 6, 11)
end_date = datetime.date(2025, 6, 10)
history_file = "history_2024.txt"
current_date = start_date

def pick_commit_count():
    r = random.random()
    if r < 0.65:
        return 0
    elif r < 0.87:
        return random.randint(1, 3)
    elif r < 0.95:
        return random.randint(4, 8)
    elif r < 0.99:
        return random.randint(10, 20)
    else:
        return random.randint(50, 60)

while current_date <= end_date:
    num_commits = pick_commit_count()

    for _ in range(num_commits):
        hour = random.randint(9, 21)
        minute = random.randint(0, 59)
        second = random.randint(0, 59)

        commit_time = datetime.datetime.combine(
            current_date, datetime.time(hour, minute, second)
        )
        date_str = commit_time.isoformat()

        with open(history_file, "a") as f:
            f.write(f"Commit on {date_str}\n")

        subprocess.run(["git", "add", "."], check=True)

        env = os.environ.copy()
        env["GIT_AUTHOR_DATE"] = date_str
        env["GIT_COMMITTER_DATE"] = date_str
        env["GIT_AUTHOR_NAME"] = "PicasoTheDeal"
        env["GIT_AUTHOR_EMAIL"] = "PicasoTheDeal@users.noreply.github.com"
        env["GIT_COMMITTER_NAME"] = "PicasoTheDeal"
        env["GIT_COMMITTER_EMAIL"] = "PicasoTheDeal@users.noreply.github.com"

        subprocess.run(
            ["git", "commit", "-m", f"Backdated commit {date_str}"],
            env=env,
            check=True,
        )

    current_date += datetime.timedelta(days=1)