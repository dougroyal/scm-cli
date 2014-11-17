Adding Custom Hosts
===================

Custom hosts need to implement a simple interface:

.. code:: python

    def get_repos(): -> list

    def clone(): -> None


There's an example client in ~/.scm/clients

After you've implemented your client, activate it by adding the name of your
custom client to the ~/.scm/scm.cfg file. See the file for an example.

get_repos()
-----------

get_repos() must return a list of dictionaries.

Each dict must contain the following keys:

    * host
    * scm_type
    * clone_url
    * name


example return value:

.. code:: python

    [
        {
            'host': HOST_ID,
            'scm_type': 'git',
            'clone_url': 'ssh:...',
            'name' : 'some unique repo name'
        },
        {
            'host': HOST_ID,
            'scm_type': 'hg',
            'clone_url': 'ssh:...',
            'name' : 'some other unique repo name'
         },
    ]

