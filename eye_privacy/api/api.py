from fastapi import FastAPI # import FastAPI class
from typing import List
from pydantic import BaseModel
import requests
import json

api = FastAPI()
api.server = "a"

class ImageSplit(BaseModel):
    id: int
    server:str
    image_arr: List[List[List[int]]]

'''
    Endpoint for receiving split by
    an intermediate server and 
    sending it to the model server
'''
@api.post("/sendimagesplit")
async def send_img_split(img: ImageSplit):
    img_dict = img.dict()
    dataJSON = json.dumps(img_dict)
    r = requests.post(url ='http://model_server:85/sendsplit/', data=dataJSON)
    # If server A, send it to replay attacker (Assumption is that the code has been altered by replay attacker)
    if api.server == img_dict["server"]:
        r1 = requests.post(url ='http://replay_adversary:90/capturesplit/', data=dataJSON)
    return r.text
