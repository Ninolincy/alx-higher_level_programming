#!/bin/bash
# Takes URL, sends a request to it, display body size of the response
curl -s "$1" | wc -c
