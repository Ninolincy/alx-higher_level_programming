#!/usr/bin/python3
#script that takes in a URL, sends a request to that URL, and displays the size of the body of the response

(curl -sI "$url" | grep -i Content-Length | awk '{print $2}')