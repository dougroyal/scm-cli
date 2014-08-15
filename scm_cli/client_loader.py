import os
import sys

# Python 3
if sys.version_info[0] >= 3:
    from configparser import ConfigParser
# Python 2
else:
    from ConfigParser import ConfigParser

# from os.path import expanduser
# USER_HOME = expanduser("~")
# SCM_RC_DIR = os.path.join(USER_HOME, '.scm')


def load_client_modules():
    clients = {}

    # TODO also search ~/.scm/host_clients/ for custom clients
    for host in _get_host_clients():
        module = "scm_cli.clients.%s_client" % host
        clients[host] = __import__(module, globals(), locals(), ['object'], 0)

    return clients


def _get_host_clients():
    config = ConfigParser()
    config.read(os.path.expanduser(os.path.join('~', '.scm', 'scm.cfg')))
    return config.sections()
