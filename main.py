from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json
import ciphers
import uvicorn

class Request(BaseModel):
    text: str
    offset: int | None 
    mode: str | None  #"encrypt" or "decrypt"

api = FastAPI()

@api.get("/")
def index():
    return {"msg":"Welcome to the hottest place in hell"}

@api.get("/test")
def testing():
    return {"msg":"Hi from test"}

@api.get("/test/{name}")
def save_name(name:str):
    with open("names.txt", "a") as f:
        f.write(name)
    return {"msg":"Saved user"}


@api.post("/caesar")
def caesar_cipher(request:Request):
    if request["mode"] == "encrypt":
        encrypted_text = ciphers.encode_ceaser(decode=request["text"], offset=request["offset"])
        return {"encrypted_text": encrypted_text}
    else:
        decrypted_text = ciphers.decode_ceaser(encode=request["text"], offset=request["offset"])
        return {"decrypted_text":decrypted_text}


@api.get("/fence/encrypt?text={text}")
def fence_cipher_encryption():
    return {"encrypted_text":""}

@api.post("/fence/decrypt")
def fence_cipher_decryption():
    return {"decrypted":""}



if __name__ == "__main__":
    uvicorn.run(api, host="localhost", port=8000)


