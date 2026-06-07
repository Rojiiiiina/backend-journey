from fastapi import FastAPI

app = FastAPI()

#Endpoint 4 - pathparameter
@app.get("/users/{name}")
async def read_name(name:str):
    return{"message":"Hello"+name}

#Endpoint 5 
@app.get("/products/{product_name}")
async def read_name(product_name:str):
    return{"product":f"You searched for {product_name}"}

#Endpoint 6
@app.get("/blog/{blog_page}")
async def read_page(blog_page:str):
    return{"blog":f"This is your {blog_page}"}