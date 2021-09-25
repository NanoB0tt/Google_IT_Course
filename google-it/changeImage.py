
#!/usr/bin/env python3

import sys
import os
from PIL import Image
path = "supplier-data/images/"
pics = os.listdir(path)
for file in pics: 
    if "tiff" in file:
        filename = os.path.splitext(file)[0]
        new = path + filename + ".jpeg"
        with Image.open(path + file) as img:
            img.resize((600,400)).convert("RGB").save(new, 'jpeg')
            img.close()


