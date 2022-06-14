from fastapi import FastAPI # import FastAPI class
import requests
import json
import numpy as np
from PIL import Image
import time

app = FastAPI()

'''
    Splits each image and sends each split
    to the server mentioned in the sequence
    along with image ID, intermediate server name
'''
def read_imgsplit(img_arr, data, server_seq):

    server_dict = {'a':81, 'b':82, 'c':83, 'd':84}
    arr_splits = np.split(img_arr,3,axis=0)
    
    data["image_arr"] = arr_splits[0].tolist()
    data["server"] = server_seq[0]
    dataJSON = json.dumps(data)
    print("Image {0} split 1 sent to {1}".format(data["id"], data["server"]))
    r1 = requests.post(url ='http://server_{0}:{1}/sendimagesplit/'.format(data["server"], server_dict[data["server"]]), data=dataJSON)
    data["image_arr"] = arr_splits[1].tolist()
    data["server"] = server_seq[1]
    dataJSON = json.dumps(data)
    print("Image {0} split 2 sent to {1}".format(data["id"], data["server"]))
    r1 = requests.post(url ='http://server_{0}:{1}/sendimagesplit/'.format(data["server"], server_dict[data["server"]]), data=dataJSON)
    data["image_arr"] = arr_splits[2].tolist()
    data["server"] = server_seq[2]
    dataJSON = json.dumps(data)
    print("Image {0} split 3 sent to {1}".format(data["id"], data["server"]))
    r1 = requests.post(url ='http://server_{0}:{1}/sendimagesplit/'.format(data["server"], server_dict[data["server"]]), data=dataJSON)
    return {"response from api":r1.text}

'''
    Endpoint to split and send images 
    (sends two images one after another)
    Calls read_imgsplit function to send the images,
    their ID number and sequence
'''
@app.get("/splitimgs")
def prepare_images():
    st = time.time()
    img = Image.open('5.jpg')
    img_arr = np.asarray(img)
    data = {"id": 101,
    }
    server_seq = "cba"
    print("\nSequence number {} and Server sequence {}\n".format(data["id"], server_seq))
    r = read_imgsplit(img_arr, data, server_seq)
    print(time.time() - st)
    
    img = Image.open('12.jpg')
    img_arr = np.asarray(img)
    data = {"id": 201,
    }
    server_seq = "dab"
    print("\nSequence number {} and Server sequence {}\n".format(data["id"], server_seq))
    r = read_imgsplit(img_arr, data, server_seq)

    return r