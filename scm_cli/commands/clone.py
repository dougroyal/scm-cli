import sys
from os import linesep
from scm_cli.repo_finder import find_repos


def clone(scm_clients, repo_pattern, clone_destination=None):

    print("hold on, I'll see if I can find that for you ...")

    repos = find_repos(scm_clients, repo_pattern)

    # if no repos are found
    if len(repos) == 0:
        print('No matches found.' + linesep)
        sys.exit('')

    # if only one match, assume that's the one the user wants
    elif len(repos) == 1:
        repo = repos[0]

    # otherwise prompt user to find out which repo to checkout
    else:
        _print_repos(repos)
        repo_index = _get_users_choice(repos)
        repo = repos[repo_index]

    the_repos_client = scm_clients[repo['host']]
    print('cloning ' + repo['name'] + ' ...')
    the_repos_client.clone(repo=repo, dest=clone_destination)
    print('clone complete. happy hacking.')


def _print_repos(repos):
    print("\nOk, here's what I got:")
    for index, repo in enumerate(repos):
        msg = '    {index}. {name}  ({host})'
        print(msg.format(index=index+1, name=repo['name'], host=repo['host']))

def _get_users_choice(repos):
    choice = 0
    number_of_repos = len(repos)

    while (choice <= 0 or choice > number_of_repos):
        choice = input('\nEnter repo number: ')
        try:
            choice = int(choice)
        except:
            # Don't respond until the user enters a valid number
            choice = 0

    return choice - 1
