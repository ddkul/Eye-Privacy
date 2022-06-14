from fastapi import FastAPI # import FastAPI class
from typing import List
from pydantic import BaseModel
import requests
import json

api = FastAPI()
api.img_arr = {}

class ImageSplit(BaseModel):
    id: int
    server:str
    image_arr: List[List[List[int]]]

'''
    Replay attacker's endpoint for
    replaying split to model server
'''
@api.get("/replaysplit")
def replay_img_split():
    img_dict = json.loads(api.img_arr)
    print("\nAdversary replaying split of image {0} captured initially from server {1}\n".format(img_dict["id"], img_dict["server"]))
    r = requests.post(url ='http://model_server:85/sendsplit/', data=api.img_arr)
    return r.text
'''
    Replay attacker's endpoint for
    capturing split directed from
    server A
'''
@api.post("/capturesplit")
def capture_replay_img_split(img: ImageSplit):
    img_dict = img.dict()
    dataJSON = json.dumps(img_dict)
    api.img_arr = dataJSON
    print("\nAdversary captured a split of image {0} from server {1}\n".format(img_dict["id"], img_dict["server"]))