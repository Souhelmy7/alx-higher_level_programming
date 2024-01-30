#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL and
displays the body of the response (decoded in utf-8)."""
import urllib.request as req
import urllib.parse as par
import urllib.error as error
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with req.urlopen(url) as response:
            content = response.read()
            print(content.decode('utf-8'))
    except error.HTTPError as er:
        print("Error code:", er.code)
