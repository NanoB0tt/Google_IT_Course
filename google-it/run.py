#!/usr/bin/env python3

import os
import requests
import json

url = "http://localhost/fruits/"
path = "supplier-data/descriptions/"
directory = os.listdir(path)

for files in directory:
    if files.endswith("txt"):
        with open(path + files, 'r') as file:
            fruitname = os.path.splitext(files)[0]
            data = file.read()
            data = data.split("\n")
            dic = {"name": data[0], "weight": int(data[1].strip(" lbs")), "description": data[2], "image_name": fruitname + ".jpeg"}
            response = requests.post(url, json=dic)

