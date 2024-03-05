from fastapi import FastAPI, Path, Query, HTTPException, status
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from typing import Optional, List
from pydantic import BaseModel

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def get_index():
    with open("index.html") as f:
        return f.read()

app.mount("/static", StaticFiles(directory="./"), name="static")

class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str] = None

class UpdateItem(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    brand: Optional[str] = None

class ItemSummary(BaseModel):
    item_id: int
    name: str

inventory = {}

@app.get("/get-all-items", response_model=List[ItemSummary])
def get_all_items():
    if len(inventory) == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No items in inventory")
    items_summary = []
    for item_id, item in inventory.items():
        item_summary = ItemSummary(item_id=item_id, name=item.name)
        items_summary.append(item_summary)
    return items_summary

@app.get("/get-item/{item_id}")
def get_item_by_id(item_id: int = Path(..., description="The ID of the item you want to view ", gt=0)):
    if item_id not in inventory:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item ID does not exist")
    return inventory[item_id]

@app.get("/get-by-name")
def get_item_by_name(name: str = Query(None, title="Name", description="Name of the item")):
    for item_id in inventory:
        if inventory[item_id].name == name:
            return inventory[item_id]
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item name not found")

@app.post("/create-item/{item_id}")
def create_item(item_id: int, item: Item):
    if len(inventory) >= 50:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Cannot create more than 50 items")
    if item_id in inventory:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Item ID already exists")
    inventory[item_id] = item
    return inventory[item_id]

@app.put("/update-item/{item_id}")
def update_item(item_id: int, item: UpdateItem):
    if item_id not in inventory:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item ID does not exist") 
    if item.name is not None:
        inventory[item_id].name = item.name
    if item.price is not None:
        inventory[item_id].price = item.price
    if item.brand is not None:
        inventory[item_id].brand = item.brand
    return inventory[item_id]

@app.delete("/delete-item")
def delete_item(item_id: int = Query(..., description="The ID of the item to delete", gt=0)):
    if item_id not in inventory:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item ID does not exist")

    del inventory[item_id]
    return {"Success": "Item deleted successfully."}