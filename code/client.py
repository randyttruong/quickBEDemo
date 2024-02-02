#!/usr/bin/env python3

# requests library: allows us to make HTTP requests
import requests

# def URL of where the Flask application is being hosted
url = "http://127.0.0.1:5000/"

# send a GET request
response = requests.get(url)

# check if successful response
if response.status_code == 200:
    # print response
    print("Response from server:", response.text)
else:
    # print error if something went wrong
    print("Failed to retrieve data. Status code:", response.status_code)
