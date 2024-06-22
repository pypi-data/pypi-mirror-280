import urllib.request
import urllib.parse
import json
import argparse

from .project_elements import Milestone


class GitlabInterface:

    def __init__(self, token, repo_url: str):
        self.token = token
        self.repo_url = f"{repo_url}/api/v4"

    def get_group_milestones(self, id: int):
        milestones_json = self.make_request(f"groups/{id}/milestones")
        milestones = [Milestone(j) for j in milestones_json]
        return milestones

    def get_project_milestones(self, id: int):
        milestones_json = self.make_request(f"projects/{id}/milestones")
        milestones = [Milestone(j) for j in milestones_json]
        return milestones

    def make_request(self, url: str):
        headers = {"Authorization": f"Bearer {self.token}"}
        full_url = f"{self.repo_url}/{url}"
        req = urllib.request.Request(full_url, headers=headers)
        with urllib.request.urlopen(req) as response:
            charset = response.headers.get_content_charset()
            if not charset:
                charset = "utf-8"
            response_str = response.read().decode(charset)
            print(response_str)
            return json.loads(response_str)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--token", type=str)
    parser.add_argument("--project_id", type=int, default=0)
    parser.add_argument("--group_id", type=int, default=0)
    parser.add_argument("--repo_url", type=str, default="https://git.ichec.ie")

    args = parser.parse_args()

    gitlab = GitlabInterface(args.token, args.repo_url)

    if args.group_id > 0:
        milestones = gitlab.get_group_milestones(args.group_id)
    else:
        milestones = gitlab.get_project_milestones(args.project_id)

    print(milestones)
