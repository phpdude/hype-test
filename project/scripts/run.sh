#!/bin/bash

# this files only pull the lastest version
cd /var/data/hype

sudo chown -R  www-data /var/data/hype

sudo service postgresql start
sudo service uwsgi start
sudo service nginx start


ls -la /var/data/hype/
ls -la /var/data/local/
ls -la /etc/nginx/sites-enabled

#git pull
#/bin/bash /var/data/hype/scripts/install.sh

#scripts/tasks/virtualenv.sh

/var/data/hype/scripts/run_test.sh

#tail /var/log/uwsgi.log

/bin/bash

tail -f /var/log/lastlog
