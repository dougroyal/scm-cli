from setuptools import find_packages
from paver.setuputils import setup
from paver.easy import task, needs, sh, path
import re
import os
import sys

VERSION = '0.1.1'

requirements = ['docopt', 'requests', 'bitbucket-api', 'PyGithub']
dev_requirements = ['wheel', 'watchdog']

# Python 3
if sys.version_info[0] >= 3:
    test_requirements = ['pytest']
# Python 2
else:
    test_requirements = ['pytest', 'mock']

setup(
    name="scm-cli",
    version="0.1.0",
    author="Doug Royal",
    author_email="douglasroyal@gmail.com",
    description=("A command line interface to various source control services, such as github, bitbucket, etc."),
    license="BSD",
    keywords="source controll",
    url="http://code.grumbleofnerds.com/scm-cli",
    packages=find_packages(exclude=['tests']),
    long_description=open('README.rst').read(),
    install_requires=requirements,
    setup_requires=dev_requirements,
    tests_require=test_requirements,
    entry_points={
        'console_scripts': ['scm = scm_cli.scm:main']
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Version Control',
        'License :: OSI Approved :: BSD License',
    ],
)


@task
@needs('build_sphinx')
def watch_docs():
    sh('watchmedo shell-command doc/source --recursive --command="paver build_sphinx"')


@task
def bump_version():
    version_line = "VERSION = '%s'" % _build_new_version(VERSION)
    version_pattern = "VERSION = '\d\.\d\.\d'"

    pavement_file = os.path.realpath(__file__)

    new_pavement_lines = []
    with open(path(pavement_file), 'r') as f:
        for line in f.readlines():
            new_line = re.sub(version_pattern, version_line, line)
            new_pavement_lines.append(new_line)

    import pprint; pprint.pprint(new_pavement_lines)

    with open(path(pavement_file), 'w') as f:
        f.writelines(new_pavement_lines)


@task
def clean():
    sh("find . -type f -name '*.pyc' -delete")


def _build_new_version(old_version):
    new_version = old_version.split('.')
    new_version[1] = str(int(new_version[1])+1)
    return '.'.join(new_version)
