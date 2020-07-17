#! /usr/bin/env python3
import os
import requests


mypath = os.path.expanduser("~/supplier-data/descriptions/")
onlyfiles = [f for f in os.listdir(mypath) if f.endswith('.txt')]

for i in onlyfiles:
	with open("{}{}".format(mypath,i)) as text_files:
		lines = text_files.read().strip().split('\n')
		dict = { "name":lines[0],"weight":int(lines[1].strip(" lbs")),"description":lines[2],"image_name":"{}.jpeg".format(i[0:3])}
		rep = requests.post("http://34.67.1.209/fruits/",data=dict)
		print(rep.status_code)
