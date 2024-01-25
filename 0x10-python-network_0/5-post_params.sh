#!/bin/bash
# Takes URL, sends a POST request to it, and displays the body of response
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
