#!/bin/bash

#run the test scripts
cd /var/data/hype/app

source /var/data/local/env/bin/activate
export CONFIG=../config/test.conf

py.test --cache-clear -v -s test_hype_container.py