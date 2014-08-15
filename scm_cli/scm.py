import sys
import argparse
from argparse import RawTextHelpFormatter

from scm_cli.commands import clone
from scm_cli.client_loader import load_client_modules


def main():

    try:
        parser = _setup_parser()
        args = parser.parse_args()

        if len(vars(args)) == 1:
            parser.print_help()
            parser.exit()

        scm_clients = load_client_modules()

        if args.command == 'clone':
            clone(scm_clients, args.repo_pattern, args.clone_destination)
        if args.command == 'create':
            print("Well, I haven't got that part done yet")

    except KeyboardInterrupt:
        sys.exit('')


def _setup_parser():
    parser = argparse.ArgumentParser(
        description="A command line utility for checking out projects from various source control systems.",
        epilog='''Examples:\n\n$ FIX ME!!!! scm foo<ENTER>\n''',
        formatter_class=RawTextHelpFormatter)

    subparsers = parser.add_subparsers(dest='command')

    clone_arg = subparsers.add_parser('clone')
    clone_arg.add_argument('repo_pattern', help='The name, or partial name, of the repository you want to clone.')
    clone_arg.add_argument('-d', dest='clone_destination',  help='The directory into which the repo will be cloned.')

    create_arg = subparsers.add_parser('create')
    create_arg.add_argument('new_repo_name', help='The name of the new repo you want to create.')
    create_arg.add_argument('-s', '--service', default='_SHOW_OPTIONS', help='The name of the scm service where the repo will be created.')

    return parser
