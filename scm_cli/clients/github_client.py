from github import Github

from scm_cli.scm_config import github_creds
from scm_cli.shell import run

USERNAME, PASSWORD = github_creds()

gh = Github(USERNAME, PASSWORD)


def get_repos():
    print('searching github ...')
    repos = gh.get_user().get_repos()

    return _format_repos(repos)


def clone(repo, dest):
    if dest == None: dest = ''

    command = 'git clone ' + repo['clone_url'] + ' ' + dest
    run(command)


def _format_repos(repos):
    formated_repos = []

    for repo in repos:
        formated_repos.append({
                'host': 'github',
                'scm_type': 'git',
                'clone_url': repo.ssh_url,
                'name' : repo.name,
            })

    return formated_repos


if __name__ == '__main__':
    from pprint import pprint
    pprint(get_repos())
