#!/bin/bash

source local/env/bin/activate
export DEBUG='False'
export PG_HOST="ec2-54-187-41-66.us-west-2.compute.amazonaws.com"
export PG_USER="hype"
export PG_DBNAME="hype_prod"
export PG_PASSWORD="passw0rd"
