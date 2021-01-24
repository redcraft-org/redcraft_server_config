import os

from git import Repo


class GitManager():

    def __init__(self):
        self.repo_location = os.path.join(os.path.dirname(__file__), '..')
        self.repo = Repo(self.repo_location)
        self.original_branch = self.repo.active_branch

    def __del__(self):
        self.switch_branch(self.original_branch)

    def switch_branch(self, branch):
        if branch not in self.repo.branches:
            self.repo.git.checkout('HEAD', b=branch)
        else:
            self.repo.git.checkout(branch)

    def push_and_create_pull_request(self):
        templates_location = os.path.join(
            self.repo_location, 'templates', '*', 'rcst_template_*.json')
        self.repo.index.add([templates_location])
        return True