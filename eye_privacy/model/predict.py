from fastapi import FastAPI # import FastAPI class
from typing import List
from pydantic import BaseModel
import numpy as np
from PIL import Image

api = FastAPI()
api.counter = 0
api.arrayCombined = [list() for i in range(3)]
api.server_seq = ["cba", "dab", "adc", "bdc"]
api.ids = [101,201,301,401]

class ImageSplit(BaseModel):
    id: int
    server:str
    image_arr: List[List[List[int]]]

# @api.get("/status")
# def read_status():
#     return api.counter

'''
    Model server endpoint for receiving the split
    The image splits ID is used to identify
    current image anticipated and the splits
    are combined.
'''
@api.post("/sendsplit")
def send_split(img: ImageSplit):
    img_dict = img.dict()
    if img_dict["id"] == api.ids[api.counter]:
        ind = api.server_seq[api.counter].index(img_dict["server"])
        api.arrayCombined[ind] = img_dict['image_arr']
        print("\nModel server received a split of image {0} from server {1}\n".format(img_dict["id"], img_dict["server"]))

    flg = True
    for l in api.arrayCombined:
        if len(l) == 0:
            flg = False
    if(flg):
        api.counter += 1
        img_arr = np.concatenate([l for l in api.arrayCombined], axis=0)
        pil_image = Image.fromarray((img_arr).astype(np.uint8))
        pil_image.save('eyesave{0}.png'.format(api.counter))
        print("\nImage {} saved by model\n".format(api.counter))
        api.arrayCombined = [list() for i in range(3)]
    return api.counter
    