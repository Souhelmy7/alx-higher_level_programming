#!/usr/bin/python3
"""script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter."""

import requests
import sys

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) > 1:
        letter = sys.argv[1]
    else:
        letter = ""
    params = {'q': letter}
    try:
        response = requests.post(url, data=params)
        response_json = response.json()
        if response_json:
            user_id = response_json.get('id', 'N/A')
            user_name = response_json.get('name', 'N/A')
            print(f"[{user_id}] {user_name}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
