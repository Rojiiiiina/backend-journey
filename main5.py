from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import Todo

app = FastAPI()

@app.post("/todos")
def create_todo(title: str, db: Session = Depends(get_db)):
    todo = Todo(title=title)
    db.add(todo)
    db.commit()
    return {"message": "Todo created!", "title": title}

@app.get("/todos")
def get_todos(db: Session = Depends(get_db)):
    todos = db.query(Todo).all()
    return todos