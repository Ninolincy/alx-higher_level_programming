#!/bin/bash
# Takes URL, sends a POST request to it, display body size of the response
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
