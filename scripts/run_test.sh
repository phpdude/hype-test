#!/bin/bash

#run the test scripts
cd /var/data/hype
source local/env/bin/activate
export CONFIG=../config/test.conf
cd api

py.test -v -s test_hype_container.py