from fastapi import FastAPI

app = FastAPI()

#Endpoint 4 - pathparameter
@app.get("/users/{name}")
async def read_name(name:str):
    return{"message":"Hello"+name}

#Endpoint 5 
@app.get("/products/{product_name}")
async def read_name(product_name:str):
    return{"products": product_name}

#Endpoint 6
@app.get("/items/{item_id}")
async def read_item(item_id:int):
    return{"item": item_id}