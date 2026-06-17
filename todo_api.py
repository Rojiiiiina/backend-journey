from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

todos = []
current_id = 1

class Todo(BaseModel):
    title: str
    completed:bool = False

@app.post("/todos/")
async def create_todo(todo:Todo):
    return todo


    

@app.get("/todos/{id}")
async def get_todo(id:int):
    return{"id":id}

@app.delete("/todos/{id}")
async def delete_todo(id:int):
    return {"message": f"Deleted todo {id}"}    