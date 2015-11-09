#!/usr/bin/env bash

# nginx config
sudo cp /var/data/hype/etc/nginx.conf /etc/nginx/sites-enabled/hype
sudo rm /etc/nginx/sites-enabled/default

# nginx config
sudo cp /var/data/hype/etc/uwsgi.ini /etc/uwsgi/apps-enabled/hype.ini