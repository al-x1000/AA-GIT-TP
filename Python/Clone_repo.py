import os
from git import Repo
git_url = "https://github.com/KeligMartin/4-SRC.git"
repo_dir = os.environ['USERPROFILE']
Repo.clone_from(git_url, repo_dir)