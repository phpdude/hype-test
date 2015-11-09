#!/usr/bin/env bash

cd /var/data/local/

curl -sL https://deb.nodesource.com/setup | sudo bash -
sudo apt-get install -y nodejs
sudo ln -s /usr/bin/nodejs /usr/bin/node
npm install bower
node_modules/.bin/bower --config.interactive=false install --allow-root
