#!/usr/bin/env python3
import requests
import os
import re

_IMGFOLDER = "./supplier-data/images/"

url = "http://localhost/upload/"

for img in os.listdir(_IMGFOLDER):
    #check if we have .JPEG image
    regex = r".*\.jpeg"
    if not re.search(regex, img.lower()):
        continue
    print("uploading: " + _IMGFOLDER + img)
    # we're good, uploading
    path = _IMGFOLDER + img
    with open(path, 'rb') as opened:
        r = requests.post(url, files={'file': opened})
