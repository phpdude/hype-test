#!/usr/bin/env bash

ENV=/var/data/local/env

virtualenv $ENV
source $ENV/bin/activate
pip install -r /var/data/hype/etc/requirements.txt