#!/usr/bin/env python3
import requests
import os

# This example shows how a file can be uploaded using
# The Python Requests module

url = "http://localhost/upload/"
mypath = os.path.expanduser("~/supplier-data/images/")
onlyfiles = [f for f in os.listdir(mypath) if f.endswith('.jpeg')]
for i in onlyfiles:
	with open('{}{}'.format(mypath,i), 'rb') as opened:
    		r = requests.post(url, files={'file': opened})
