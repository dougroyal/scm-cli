"""
Usage:
    scm clone (REPO)

A utility for checking out repositories from various source control systems.

Required:
    REPO The name, or partial name, of the repository you want to search for and checkout.
"""
import os
from shutil import copytree
import sys
import docopt

from scm_cli.commands import clone
from scm_cli.client_loader import load_client_modules


def main():
    try:

        args = docopt.docopt(__doc__)

        init_if_first_run()

        scm_clients = load_client_modules()

        if args['clone']:
            clone(scm_clients, repo_pattern=args['REPO'])

    except KeyboardInterrupt:
        sys.exit('')


def init_if_first_run():
    """
    Check if rc files exist.
    Initialize rc dirs and files if necessary
    """
    scm_cfg_file = os.path.expanduser(os.path.join('~', '.scm', 'scm.cfg'))

    if scm_cfg_file:
        message = """\

Looks like this is the first time you've run scm.

I'll setup a config file for you.

## IMPORTANT ##
You need to edit ~/.scm/scm.cfg to add the necessary credentials.
-----------------------------------------------------------------

You can also use this directory to add custom scm host clients.

See the docs at http://code.grumbleofnerds.com/scm-cli for more information.

"""
        print(message)

        dest = os.path.join(os.path.expanduser("~"), '.scm')
        scm_src = os.path.dirname(os.path.abspath(__file__))
        assets_dir = os.path.join(scm_src, 'assets')

        copytree(assets_dir, dest)
        sys.exit()