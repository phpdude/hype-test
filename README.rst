Test Code Audition Web Python Developers
-------------

All you have to do to get the app working is to follow the instruction:

.. code-block:: console

    $ curl -sSL https://raw.githubusercontent.com/gpisacco/hype_test/master/scripts/base.sh | sh

All you need to bring the API online is to create a docker container
it  gets the code from git , deploys it and runs a small curl checking script
(the computer needs to have docker installed)

To run the unit test scripts :

.. code-block:: console

    $ docker exec <container_id> /var/data/hype/scripts/run_test.sh

Features
--------
* Admin Login
* User Login

Notes
--------
* All the services (postgres,nginx and uwsgi) are running in the same container due to time restrictions
* Unit tests and production uses different databases , they are configured via an env varable