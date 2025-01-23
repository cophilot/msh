import requests
import json
import os


def main():
    releases = get_releases()


def get_all_commits():
    command = "git log --pretty=format:'%h %ad|%s%d' --date=short --no-merges"
    commits_log = os.popen(command).read().split("\n")

    print(commits_log)
    commits = []

    for commit in commits_log:
        commit = commit.split("|")
        message = commit[1]
        if message.startswith("update:"):
            continue
        commits.append(
            {
                "date": commit[0].split(" ")[1],
                "message": commit[1],
            }
        )
    print(json.dumps(commits, indent=4))
    return commits


def get_releases():
    realeses_url = "https://api.github.com/repos/cophilot/msh/releases"
    releases_raw = requests.get(realeses_url).json()
    realeses = []
    all_commits = get_all_commits()
    for release in reversed(releases_raw):
        commits = []
        for index, commit in enumerate(all_commits):
            if commit is None:
                continue
            if compare_dates(commit["date"], release["published_at"]) == 1:
                continue
            commits.append(commit)
            all_commits[index] = None

        realeses.append(
            {
                "date": release["published_at"],
                "date_" "url": release["html_url"],
                "name": release["name"],
                "commits": commits,
            }
        )
    print(json.dumps(realeses, indent=4))
    return realeses


def compare_dates(date1, date2):
    date1 = date1.split("T")[0]
    date2 = date2.split("T")[0]
    date1 = date1.split("-")
    date2 = date2.split("-")
    for i in range(3):
        if date1[i] < date2[i]:
            return -1
        elif date1[i] > date2[i]:
            return 1
    return 0


if __name__ == "__main__":
    main()
