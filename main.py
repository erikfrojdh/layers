# from typing import Union

from fastapi import FastAPI, Request
import json
from pydantic import BaseModel
app = FastAPI()

from slsdet import Detector

@app.get("/")
def read_root():
    d = Detector()
    return str(d.versions)

# @app.get("/det/")
# def read(property):
#     d = Detector()
#     val = getattr(d, property)
#     msg = json.dumps({property:val})
#     return msg

# @app.post("/det/{item}/")
# def write(item):
#     print(f'{item=}')
#     return item


# @app.post("/set/{item}/")
# def write(item):
#     print(f'{item=}')
#     return item




class Item(BaseModel):
    name: str
    value: str | int| float = None
    

@app.get('/det')
def read():
    print('hej')

@app.post('/det')
async def write(req : Request):
    json_req = await req.json()
    d = Detector()
    for key, value in json_req.items():
        setattr(d, key, value)
        print(f'Setting {key} to {value}')

    # return req
    # print(f'{req}')