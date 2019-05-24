from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import HTTPException


app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None

class Message(BaseModel):
    message: str


@app.get("/")
def read_root():
    return "SELAB"

@app.get("/items/{item_id}", responses={404: {"model": Message}})
def read_item(item_id: int, q: str = None):
    if item_id == 10:
        raise HTTPException(status_code=404, content = {"message":"Item not found"})
    return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}")
def create_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}


