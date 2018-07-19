#!/bin/bash
docker run -p 8091:80 --rm --name=tools-example-instance tools-example && echo "You can connect to http://localhost:8091"