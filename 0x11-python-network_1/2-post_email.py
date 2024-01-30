#!/usr/bin/python3
"""Python script that takes in a URL and an email, sends a POST request to the
passed URL with the email as a parameter, and displays the body of the response
(decoded in utf-8)"""
import urllib.parse
import urllib.request as URL
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    params = {'email': email}
    data = urllib.parse.urlencode(params)
    data = data.encode('ascii')
    req = URL.Request(url, data)
    with URL.urlopen(req) as response:
        content = response.read()
        print(content.decode('utf-8'))
