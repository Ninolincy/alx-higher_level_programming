#!/usr/bin/python3
"""
Takes in a URL and an email address, sends a POST request to the passed
 URL with the email as a parameter, and displays the body of the 
 response (decoded in utf-8)
 """

import urllib.request
import sys


if __name__ == "__main__":    
    with urllib.request.urlopen(sys.argv[1], 
                                'email=' + sys.argv[2].encode()) as response:
        print(response.read().decode("utf-8"))
