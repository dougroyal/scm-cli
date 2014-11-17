User Guide
==========

.. code:: bash

    $ scm clone <PROJECT>

**PROJECT** can be a partial name. For example:

.. code:: bash

    $ scm clone bones

might present you with the following:

.. code:: bash

    $ scm clone bones
    hold on, I'll see if I can find that for you ...
    searching github ...
    searching bitbucket ...

    Ok, here's what I got:
        1. bones-testing  (github)
        2. bones-testing-private  (bitbucket)
        3. bones-testing-deleteme  (bitbucket)

    Enter repo number:

**If scm only finds one match, it will automatically check out that project.**
