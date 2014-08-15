import requests
import json
from uuid import uuid4
import re

from colorama import Fore, Back, Style
from colorama import init
init(autoreset=True)
# Colorama options
# Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
# Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
# Style: DIM, NORMAL, BRIGHT, RESET_ALL


from scm_cli.config import config

api_path = '/_admin/api'
protocol_pattern = re.compile('(https?://)(.*)')


def get_repos():
    try:
        url = '{host}{path}'.format(
            host=config['rhodecode']['host'],
            path=api_path
        )

        payload = {'id': str(uuid4()),
                'api_key': config['rhodecode']['api_key'],
                'method': 'get_repos',
                'args': {'': ''},
                }

        response = requests.post(url, json.dumps(payload)).json()
    except:
        print(Back.BLACK + Fore.YELLOW + 'WARNING: unable to connect to rhodecode server')
        return None

    return _normalize_fields(response['result'])


def _normalize_fields(json_string):

    for repo in json_string:

        repo['name'] = repo['repo_name']
        repo['scm_type'] = repo['repo_type']

        # build clone url
        matches = protocol_pattern.match(config['rhodecode']['host'])
        repo['clone_url'] = '{protocol}{username}@{host}/{repo}'.format(
            protocol=matches.group(1),
            username=config['rhodecode']['username'],
            host=matches.group(2),
            repo=repo['repo_name'])

    return json_string


if __name__ == '__main__':
    from pprint import pprint
    pprint(get_repos())
