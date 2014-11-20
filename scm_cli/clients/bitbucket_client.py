from bitbucket.bitbucket import Bitbucket

from scm_cli.scm_config import bitbucket_creds
from scm_cli.shell import run

USERNAME, PASSWORD = bitbucket_creds()
bb = Bitbucket(USERNAME, PASSWORD)

def get_repos():
    print('searching bitbucket ...')
    success, repos = bb.repository.all()

    return _format_repos(repos)


def clone(repo, dest):

    if dest == None: dest = ''

    if repo['scm_type'] == 'git':
        clone_url = 'git@bitbucket.org:{USERNAME}/{REPO_NAME}.git {DESTINATION}'.format(
                        USERNAME=USERNAME, REPO_NAME=repo['name'], DESTINATION=dest)
        command = 'git clone ' + clone_url
        run(command)

    elif repo['scm_type'] == 'hg':
        clone_url = 'ssh://hg@bitbucket.org/{USERNAME}/{REPO_NAME} {DESTINATION}'.format(
                        USERNAME=USERNAME, REPO_NAME=repo['name'], DESTINATION=dest)
        command = 'hg clone ' + clone_url +' '+ dest
        run(command)


def _format_repos(repos):
    formated_repos = []

    for repo in repos:
        formated_repos.append({
                'host': 'bitbucket',
                'clone_url': '',
                'scm_type' : repo['scm'],
                'name' : repo['slug'],
            })

    return formated_repos


if __name__ == '__main__':
    from pprint import pprint
    pprint(get_repos())
