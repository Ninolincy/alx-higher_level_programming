#!/bin/bash
# Takes URL, sends a DELETE request to it, display body size of the response
curl - sX DELETE "$1"
