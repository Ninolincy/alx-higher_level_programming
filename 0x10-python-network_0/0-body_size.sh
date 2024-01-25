#!/usr/bin/bash
# Takes URL, sends a request to it, display body size of the response
(curl - sI "$url" | grep - i "Content-Length" | awk '{print $2}')
