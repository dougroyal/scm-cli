import sys
from os import linesep
from scm_cli import printer
from scm_cli.repo_finder import find_repos


def clone(scm_clients, repo_pattern, clone_destination):

    printer.notify_starting_search()

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
        printer.display_options(repos)
        repo_index = _get_users_choice(repos)
        repo = repos[repo_index]

    the_repos_client = scm_clients[repo['host']]
    the_repos_client.clone(repo=repo, dest=clone_destination)


def _get_users_choice(repos):
    choice = 0
    number_of_repos = len(repos)

    while (choice <= 0 or choice > number_of_repos):
        try:
            choice = int(input('Enter repo number: '))
        except Exception as e:
            pass # Don't respond until the user enters a valid number

    return choice - 1
