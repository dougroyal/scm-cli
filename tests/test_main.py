import pytest
from unittest.mock import MagicMock

from scm_cli import scm


def test_should_print_help_msg_when_initializing_rc_dir(capsys):
    scm.docopt = MagicMock()
    scm.copytree = MagicMock()
    scm.os.path.isfile = MagicMock()
    scm.os.path.isfile.return_value = False

    expected_message = """\

Looks like this is the first time you've run scm.

I'll setup a config file for you.

## IMPORTANT ##
You need to edit ~/.scm/scm.cfg to add the necessary credentials.
-----------------------------------------------------------------

You can also use this directory to add custom scm host clients.

See the docs at http://code.grumbleofnerds.com/scm-cli for more information.


"""

    with pytest.raises(SystemExit):
        scm.main()

    out, err = capsys.readouterr()

    assert expected_message == out


def test_should_copy_rc_files_when_initializing_rc_dir():
    scm.docopt = MagicMock()
    scm.copytree = MagicMock()
    scm.os.path.isfile = MagicMock()
    scm.os.path.expanduser = MagicMock()
    scm.os.path.abspath = MagicMock()

    scm.os.path.isfile.return_value = False
    scm.os.path.expanduser.return_value = "/path/to/fakeuser/"
    scm.os.path.abspath.return_value = "/path/to/scm/"

    with pytest.raises(SystemExit):
        scm.main()

    scm.copytree.assert_called_with('/path/to/scm/assets', '/path/to/fakeuser/.scm')
