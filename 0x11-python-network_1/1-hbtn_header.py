#!/usr/bin/python3
"""Module that takes in a URL, sends a request to the URL and displays the value of the X-Request-Id"""
import urllib.request
import sys


if __name__ == "__main__":
    with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as response:
        print(response.headers.get("X-Request-Id"))
