#!/usr/bin/env bash

sudo service postgresql restart
#sleep 10
#postgres production configuration
sudo -u postgres psql -c "CREATE DATABASE hype_prod;"
sudo -u postgres psql -c "CREATE USER hype WITH PASSWORD 'passw0rd';"
sudo -u postgres psql -d hype_prod -c "CREATE SCHEMA lbs2 AUTHORIZATION hype;"
sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE hype_prod TO hype;"
sudo -u postgres psql -d hype_prod -c "ALTER DEFAULT PRIVILEGES IN SCHEMA lbs2 GRANT ALL PRIVILEGES ON tables TO hype;"
sudo -u postgres psql -d hype_prod -a -f /var/data/hype/etc/schema.sql
sudo -u postgres psql -d hype_prod -c " GRANT SELECT, USAGE  ON ALL SEQUENCES IN SCHEMA lbs2 TO hype;"

#postgres test configuration
sudo -u postgres psql -c "CREATE DATABASE hype_test;"
sudo -u postgres psql -c "CREATE USER hype_test WITH PASSWORD 'passw0rd';"
sudo -u postgres psql -d hype_test -c "CREATE SCHEMA lbs2 AUTHORIZATION hype_test;"
sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE hype_test TO hype_test;"
sudo -u postgres psql -d hype_test -c "ALTER DEFAULT PRIVILEGES IN SCHEMA lbs2 GRANT ALL PRIVILEGES ON tables TO hype_test;"
sudo -u postgres psql -d hype_test -a -f /var/data/hype/etc/schema.sql
sudo -u postgres psql -d hype_test -c " GRANT SELECT, USAGE  ON ALL SEQUENCES IN SCHEMA lbs2 TO hype_test;"