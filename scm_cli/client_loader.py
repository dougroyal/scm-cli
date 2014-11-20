import os
import sys
from importlib import import_module

# Python 3
if sys.version_info[0] >= 3:
    from configparser import ConfigParser
# Python 2
else:
    from ConfigParser import ConfigParser

from os.path import expanduser
USER_HOME = expanduser("~")
SCM_RC_DIR = os.path.join(USER_HOME, '.scm')
CUSTOM_CLIENTS_DIR = os.path.join(SCM_RC_DIR, 'clients')

# enable ~/.scm/clients
sys.path.append(CUSTOM_CLIENTS_DIR)

def load_client_modules():
    clients = {}

    for host in _get_host_clients():
        try:
            module = '.%s_client' % host
            clients[host] = import_module(module, 'scm_cli.clients')
        except:
            clients[host] = import_module(host)

    return clients


def _get_host_clients():
    config = ConfigParser()
    config.read(os.path.expanduser(os.path.join('~', '.scm', 'scm.cfg')))
    return config.sections()
