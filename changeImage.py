
#!/usr/bin/env python3

import PIL
from PIL import Image
import os
import re

#image folder location
_SOURCE = "./supplier-data/images/"
#desired location
_DESTINATION = "./supplier-data/images/"
#desired pic resolution
_NEWSIZE = (600, 400)
#current format to be converted
_OLDFORMAT = ".jpg"
#desired format
_NEWFORMAT = "jpeg"
#rotation angle
_ANGLE = 0

#debug switch
_DEBUG = False

#converts single image to preset format and size
def resize(img, size):
    return img.resize(size)

#rotate image angle degrees counter-clockwise
def rotate_image(img, angle):
    return img.rotate(angle)

#print wrapper for debugging
def d_print(s):
    if _DEBUG == True:
        print(s)

for file in os.listdir(_SOURCE):
    d_print(file)
    #regex = r"(.*)\." + _OLDFORMAT[1:]
    #d_print(regex)
    #m = re.search(regex, file)
    #if m == None:
    #    continue
    #d_print(m)
    #d_print(m.group(1))
    try:
        current_image = Image.open(_SOURCE + file)
    except PIL.UnidentifiedImageError:
        #not an image, no need to convert
        continue
    name = file.split(".")
    current_image = resize(rotate_image(current_image, _ANGLE), _NEWSIZE)
    if current_image.mode != "RGB":
        current_image = current_image.convert("RGB")
    current_image.save(_DESTINATION + name[0] + "." + _NEWFORMAT, format=_NEWFORMAT)
