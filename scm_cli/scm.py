"""Usage: scm clone [REPO]

A utility for checking out repositories from various source control systems.

Required:
    REPO The name, or partial name, of the repository you want to search for and checkout.
"""
import sys
import docopt

from scm_cli.commands import clone
from scm_cli.client_loader import load_client_modules


def main():
    try:

        args = docopt.docopt(__doc__)

        scm_clients = load_client_modules()

        if args['clone']:
            clone(scm_clients, repo_pattern=args['REPO'])

    except KeyboardInterrupt:
        sys.exit('')
