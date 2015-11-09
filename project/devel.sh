#!/bin/bash

cd `dirname $0`

docker ps -a | awk '$2=="hype_container" { print $1 }' | xargs docker rm -f > /dev/null
docker build -t hype_container .

docker run -d -p 8085:80 -v `pwd`:/var/data/hype hype_container