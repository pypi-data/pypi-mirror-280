#!/usr/bin/env python3
"""
Copyright (C) 2024 Checkmk GmbH - License: GNU General Public License v2
This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
conditions defined in the file COPYING, which is part of this source code package.

"""

import json
import os
import sys
from contextlib import suppress
from datetime import datetime

from jira import JIRA
from requests import ReadTimeout
from rich import print as rich_print
from trickkiste.misc import age_str, date_from, date_str

EXPORT_FILE = "jira_issues.json"
FIELDS = [
    # 'comment',
    "summary",
    "description",
    "issuetype",
    "created",
    "status",
    "creator",
    "versions",
    "reporter",
    "assignee",
    "fixVersions",
    "components",
    "votes",
    "priority",
]
JIRA_BASE_URL = "https://jira.lan.tribe29.com"


def extract(issue, extract_comments=False):
    fields = issue.raw["fields"]

    if extract_comments:
        comments = fields["comment"]["comments"]
        import yaml

        for c in comments:
            if c["author"]["name"] == "frans.fuerst":
                print(issue.raw["id"], issue.raw["key"])
                print(c["body"])

    return {
        "id": issue.raw["id"],
        "key": issue.raw["key"],
        "summary": fields["summary"],
        "description": fields["description"],
        "creator": (fields.get("creator") or {"displayName": "None"})["displayName"],
        "reporter": (fields.get("reporter") or {"displayName": "None"})["displayName"],
        "assignee": (fields.get("assignee") or {"displayName": "None"})["displayName"],
        "created": fields["created"],
        "status": fields["status"]["name"],
        "versions": [v["name"] for v in fields["versions"]],
        "fixVersions": [v["name"] for v in fields["fixVersions"]],
        "components": [c["name"] for c in fields["components"]],
        "priority": fields["priority"]["name"],
        "votes": fields["votes"]["votes"],
        "issuetype": fields["issuetype"]["name"],
    }


def load_issues(filename):
    with suppress(FileNotFoundError):
        return json.load(open(filename))
    return {}


def fetch_issues(jira, proj, issues):
    while True:
        issues_chunk = [
            extract(issue)
            for issue in jira.search_issues(
                jql_str=f"project={proj} and assignee = currentUser()",
                # jql_str=f'project={proj}',
                startAt=len(issues),
                maxResults=500,
                fields=",".join(FIELDS),
            )
        ]
        if not issues_chunk:
            break
        issues.extend(issues_chunk)
        print(
            len(issues),
            issues_chunk[-1]["id"],
            issues_chunk[-1]["key"],
            issues_chunk[-1]["created"],
        )


def main():
    finalized_issues = {
        "SUP-11861",
        "SUP-11895",
        "SUP-12040",
        "SUP-12068",
        "SUP-12092",
    }
    jira = JIRA(
        server="https://jira.lan.tribe29.com",
        basic_auth=open(os.path.expanduser("~/.cmk-credentials-me"))
        .readline()
        .strip("\n")
        .split(":"),
        validate=True,
        # timeout=1,
    )
    issues = [
        i
        for i in jira.search_issues("assignee was frans.fuerst", maxResults=10000)
        if i.key not in finalized_issues
    ]

    print("Read issues from file..")
    # try:
    #    for proj in {'CMK', 'SUP', 'FEED', 'ERP', 'AQ'}:
    #        print(f"Fetch issues for project {proj!r}")
    #        fetch_issues(jira, proj, projects.setdefault(proj, []))
    # finally:
    #    print("Dump issues to file..")
    #    json.dump(projects, open(EXPORT_FILE, "w"), indent=2)
    rich_print(
        "\n".join(
            (
                f"{j.fields.created[:10]}"
                f" [link={JIRA_BASE_URL}/browse/{j.key}]{j.key:10s} - {j.fields.summary}[/]"
                f" {str(j.fields.status):20s}"
                # f"r={str(i['reporter']):22} "
                # f"a={str(i['assignee']):22} "
                # f"f={str(i['fixVersions'] and i['fixVersions'][0]):10} "
            )
            for j in sorted(issues, key=lambda i: i.fields.created)
            if str(j.fields.status) not in {"Closed", "Resolved"}
        )
    )


if __name__ == "__main__":
    main()
