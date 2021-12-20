#!/usr/bin/env python3
import requests
import os

#data folder location
_SOURCE = "./supplier-data/descriptions/"
#web-api url
_API="http://34.123.106.62/fruits/"

#debug switch
_DEBUG=False
#print for debug-output
def d_print(s):
    if _DEBUG == True:
        print(s)

def make_json(id, name, weight, desc, image):
    desc = {"id":id, "name":name, "weight":weight, "description":desc, "image_name":image}
    return desc

#sends data to web-sevice via API
def send_data(rev):
    response = requests.post(_API, json=rev)
    d_print(response.status_code)
    d_print(response.text)

data = []
cnt = 0
for file in os.listdir(_SOURCE):
    with open(_SOURCE+file, 'r') as f:
        name = f.readline()
        weight = f.readline().split()[0]
        desc = f.readline()
        image = file.split(".")[0] + ".jpeg"
        data.append(make_json(cnt, name, weight, desc, image))
        cnt = cnt + 1
        #converted = convert_reviews(review_data)
d_print(data)
for rev in data:
    send_data(rev)
