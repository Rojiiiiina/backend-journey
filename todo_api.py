from fastapi import FastAPI
from pydantic import BaseModel

class Todo(BaseModel):
    title: str
    
app = FastAPI()

@app.post("/todos/")
async def create_todo(todo: Todo):
    return todo

@app.get("/todos/{id}")
async def get_todo(id:int):
    return{"id":id}

@app.delete("/todos/{id}")
async def delet_todo(id:int):
    return {"message": f"Deleted todo {id}"}