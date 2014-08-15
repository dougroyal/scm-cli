import os
from setuptools import setup, find_packages
from setuptools.command.install import install
from shutil import copytree

requirements = ['requests', 'colorama', 'bitbucket-api', 'PyGithub']

class CustomInstallCommand(install):
    """Customized setuptools install command - sets up user preferences and custom plugin's directory."""

    def run(self):
        user_home = os.path.expanduser("~")
        dest = os.path.join(user_home, '.scm')

        # copy default files to user's scm cfg dir
        this_dir = os.path.dirname(os.path.abspath(__file__))
        assets_dir = os.path.join(this_dir, 'assets')

        copytree(assets_dir, dest)

        install.run(self)


setup(
    name="scm-cli",
    version="0.0.4",
    author="Doug Royal",
    author_email="douglasroyal@gmail.com",
    description=("A command line interface to various source control services, such as github, bitbucket, etc."),
    license="PSF",
    keywords="source controll",
    url="http://houseofquark.com/scm-cli",
    packages=find_packages(),
    long_description=open('README.rst').read(),
    install_requires=requirements,
    cmdclass={ 'install': CustomInstallCommand, },
    entry_points={
        'console_scripts': ['scm = scm_cli.scm:main']
    },
    setup_requires=['wheel'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Version Control',
        'License :: OSI Approved :: Python Software Foundation License',
    ],
)
