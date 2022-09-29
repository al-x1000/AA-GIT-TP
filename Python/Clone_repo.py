###############################################################
#                                                             #
#               Script to clone a specific repo.              #
#                                                             #
#                                                             #
#              HUELLOU Alexis, TAILLANDER Aliaume             #
#                                                             #
###############################################################

# Based on Python3

import os
from git import Repo
git_url = "https://github.com/KeligMartin/4-SRC.git"
repo_dir = os.environ['USERPROFILE']
Repo.clone_from(git_url, repo_dir)