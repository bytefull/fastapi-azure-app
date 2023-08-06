from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

fake_db = []


class Item(BaseModel):
    id: int
    name: str
    price: float
    is_early_bird: Optional[bool] = None


@app.get("/")
def root():
    return {"message": "hello world"}


@app.get("/items")
def get_items():
    return fake_db


@app.get("/items/{item_id}")
def get_item(item_id: int):
    item = item_id - 1
    return fake_db[item]


@app.post("/items")
def add_item(item: Item):
    fake_db.append(item.model_dump())
    return fake_db[-1]


@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    fake_db.pop(item_id - 1)
    return {"message": "deleted successfully"}
