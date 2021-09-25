#!/usr/bin/env python3

import requests
import os
url = "http://localhost/upload/"
directory = "supplier-data/images/"
path = os.listdir(directory)
for file in path:
    if file.endswith(".jpeg"):
        with open(directory + file, 'rb') as opened:
            r = requests.post(url, files={'file': opened})

