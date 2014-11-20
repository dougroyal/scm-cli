import sys
import pytest

# Python 3
if sys.version_info[0] >= 3:
    from unittest.mock import MagicMock
# Python 2
else:
    from mock import MagicMock


# Python 3
if sys.version_info[0] >= 3:
    from configparser import ConfigParser
# Python 2
else:
    from ConfigParser import ConfigParser

from scm_cli import scm_config


def test_should_exit_with_message_when_no_bitbucket_credentials():
    scm_config.config = MagicMock()
    scm_config.config.get.return_value = None

    with pytest.raises(SystemExit) as error:
        scm_config.bitbucket_creds()

    assert str(error.value) == '\nYou need to add your credentials to ~/.scm/scm.cfg bitbucket section.\n'


def test_should_exit_with_message_when_no_github_credentials():
    scm_config.config = MagicMock()
    scm_config.config.get.return_value = None

    with pytest.raises(SystemExit) as error:
        scm_config.github_creds()

    assert str(error.value) == '\nYou need to add your credentials to ~/.scm/scm.cfg github section.\n'


def test_should_return_github_credentials():
    username = 'howdy'
    password = 'pardner'

    config = ConfigParser()
    config.add_section('github')
    config.set(section='github', option='username', value=username)
    config.set(section='github', option='password', value=password)

    scm_config.config = config

    actual_username, actual_password = scm_config.github_creds()

    assert username == actual_username
    assert password == actual_password


def test_should_return_bitbucket_credentials():
    username = 'howdy'
    password = 'pardner'

    config = ConfigParser()
    config.add_section('bitbucket')
    config.set(section='bitbucket', option='username', value=username)
    config.set(section='bitbucket', option='password', value=password)

    scm_config.config = config

    actual_username, actual_password = scm_config.bitbucket_creds()

    assert username == actual_username
    assert password == actual_password
