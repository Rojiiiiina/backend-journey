from fastapi import FastAPI
app = FastAPI()

fake_items_db = [{"item_name":"foo"}, {"item_name":"goo"}]
@app.get("/items/")
async def reat_item(skip:int = 0, limit: int =10):
    return fake_items_db[skip: skip + limit]