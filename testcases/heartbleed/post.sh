#!/bin/bash

[[ -n "$PORT" ]] || { echo "Error: PORT is not set."; exit 1; }

echo "Simulating login with username=$1 and password=$2"
curl -k -s -m .1 -d "username=$1&password=$2" https://localhost:$PORT/submit%
