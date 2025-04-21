#***Basic FastAPI App with a Root GET Endpoint***
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"Hello": "World"}

#------------------------------------------------------------------
#***Simple POST and GET with In-Memory Item List***
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

items = []

class Item(BaseModel):
    name: str

@app.post("/items")
def add_item(item: Item):
    items.append(item.name)
    return {"message": "Item added", "item": item.name}

@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {"item": items[item_id]}
#------------------------------------------------------------------
#***GET Endpoint with 404 Error Handling for Missing Items***
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

items = []

class Item(BaseModel):
    name: str

@app.post("/items")
def add_item(item: Item):
    items.append(item.name)
    return {"message": "Item added", "item": item.name}

@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id < len(items):
        return {"item": items[item_id]}
    else:
        raise HTTPException(status_code=404, detail=f"Item {item_id} not found")
#----------------------------------------------------------------
#***List Items with Query Parameter Limit (Simple Pagination)***
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

items = []

class Item(BaseModel):
    name: str

@app.post("/items")
def add_item(item: Item):
    items.append(item.name)
    return {"message": "Item added", "item": item.name}

@app.get("/items/{item_id}")
def get_item(item_id: int):
    if 0 <= item_id < len(items):
        return {"item": items[item_id]}
    else:
        raise HTTPException(status_code=404, detail=f"Item {item_id} not found")

@app.get("/items/")
def list_items(limit: int = 10):
    return {"items": items[0:limit]}
#------------------------------------------------------------------
#***FastAPI with Pydantic: Task List API (GET, POST)***
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Item(BaseModel):
    text: Optional[str] = None
    is_done: bool = False

items = []

@app.post("/items", response_model=Item)
def create_item(item: Item):
    items.append(item)
    return item

@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    if 0 <= item_id < len(items):
        return items[item_id]
    else:
        raise HTTPException(status_code=404, detail="Item not found")

#------------------------------------------------------------------
#***List Items with Query Parameter Limit (Simple Pagination)***
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI()

class Item(BaseModel):
    text: Optional[str] = None
    is_done: bool = False

items: List[Item] = []

@app.post("/items", response_model=Item)
def create_item(item: Item):
    items.append(item)
    return item

@app.get("/items", response_model=List[Item])
def list_item(limit: int = 10):
    return items[:limit]

@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    if 0 <= item_id < len(items):
        return items[item_id]
    raise HTTPException(status_code=404, detail="Item not found")
