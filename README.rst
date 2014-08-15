smc-cli
=======

If you have lots of projects stored in lots of places, you probably waste time trying to hunt down your source code.

This is a command line utility that will search whatever hosts you configure and check out your projects for you.


Currently supported
-------------------

Linux                                                                                                                                  

Python 2.7 or 3+ 

git, mercurial

github, bitbucket

custom git or mercurial hosts are supported via a simple plugin system

Usage
-----
Afte you install, edit ~/.scm/scm.cfg

Add usernames and passwords

then:

$ scm clone <some pattern>
