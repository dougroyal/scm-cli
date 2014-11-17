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

    if not username or not password:
        sys.exit('\nYou need to add your credentials to ~/.scm/scm.cfg bitbucket section.\n')

    return username, password

def github_creds():
    username = config.get('github', 'username')
    password = config.get('github', 'password')

    if not username or not password:
        sys.exit('\nYou need to add your credentials to ~/.scm/scm.cfg github section.\n')

    return username, password
