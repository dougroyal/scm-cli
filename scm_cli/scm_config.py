import os
import sys

# Python 3
if sys.version_info[0] >= 3:
    from configparser import ConfigParser
# Python 2
else:
    from ConfigParser import ConfigParser

config = ConfigParser()
config.read(os.path.expanduser(os.path.join('~', '.scm', 'scm.cfg')))

def bitbucket_creds():
    username = config.get('bitbucket', 'username')
    password = config.get('bitbucket', 'password')

    return username, password

def github_creds():
    username = config.get('github', 'username')
    password = config.get('github', 'password')

    return username, password
