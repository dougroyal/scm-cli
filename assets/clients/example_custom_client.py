"""
Example client plugin

Required interface:

def get_repos(): -> list
    example return value:
    [
        {
            'host': HOST_ID,
            'scm_type': 'git',
            'clone_url': 'ssh:...',
            'name' : 'some unique repo name'
        },
        {
            'host': HOST_ID,
            'scm_type': 'hg',
            'clone_url': 'ssh:...',
            'name' : 'some other unique repo name'
         },
    ]

def clone(): -> None
"""

from scm_cli.shell import run

HOSTNAME = 'example.com' # The name of your internal server that has your repos
STORAGE_DIR = '/storage/repos/'

MERCURIAL = 'hg'
GIT = 'git'


def get_repos():
    git_repos = run(['ssh', HOSTNAME, 'ls '+STORAGE_DIR+GIT])
    hg_repos = run(['ssh', HOSTNAME, 'ls '+STORAGE_DIR+MERCURIAL])

    repos = []
    repos.extend(_format_repos(git_repos, GIT))
    repos.extend(_format_repos(hg_repos, MERCURIAL))

    return repos


def clone(repo, dest):
    if dest == None: dest = ''
    run([repo['repo_type'], 'clone', repo['clone_url'], dest])


def _format_repos(repos, repo_type):
    formated_repos = []

    for repo in repos.split():
        clone_url = 'ssh://'+HOSTNAME+'/'+STORAGE_DIR+'/'+repo_type+'/'+repo

        formated_repos.append({
                'host': HOSTNAME,
                'clone_url': clone_url,
                'scm_type' : repo_type,
                'name' : _format_name(repo, repo_type)
            })

    return formated_repos


def _format_name(name, repo_type):

    if repo_type == MERCURIAL:
        return name
    if repo_type == GIT:
        return ''.join(name.split('.')[:-1])


def _determine_type(repo):
    if repo.endswith('.hg'):
        return 'mercurial'
    elif repo.endswith('.git'):
        return 'git'


if __name__ == '__main__':
    from pprint import pprint
    pprint(get_repos())
