from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float

# In-memory storage for items (Change made: Added dictionary to store items)
items = {}

@app.post("/items/")
async def create_item(item: Item):
    # Check for negative price (Change made: Raised HTTPException instead of ValueError for proper error handling)
    if item.price < 0:
        raise HTTPException(status_code=400, detail="Price cannot be negative")
    
    # Assign a unique ID to each item (Change made: Store items with unique IDs in memory)
    item_id = len(items) + 1  
    items[item_id] = item
    # Return the item with its assigned ID (Change made: Included item ID in the response)
    return {"id": item_id, "name": item.name, "price": item.price}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    # Retrieve the item by its ID (Change made: Call to the new helper function get_item_by_id)
    item = get_item_by_id(item_id)
    return item

def get_item_by_id(item_id: int):
    # Check if the item exists in storage (Change made: Check existence and raise HTTPException if not found)
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    
    return items[item_id]  # Return the found item

"""
1.Implementation of get_item_by_id: I implemented this function to look up an item by its ID. If the item doesn't exist, it raises an HTTPException with a 404 status code and a relevant error message.

2.In-Memory Item Storage: Introduced a dictionary items to store the created items. The keys are unique item IDs, allowing us to retrieve items by their ID later.

3.Error Handling with HTTPException:  Changed the handling of negative prices to raise an HTTPException instead of ValueError. This provides a proper HTTP error response (status code 400) when the price is negative.

4. Item ID Generation: When an item is created, I generate a unique ID based on the length of the items dictionary, ensuring each item has a unique identifier.

5. Return Values: When creating an item, the response now includes the item ID for easier reference in future requests.
"""