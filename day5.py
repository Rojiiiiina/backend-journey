from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import DeclarativeBase
engine = create_engine("postgresql://postgres:9840@localhost/backenddb")

print("Database created successfully")

class Base(DeclarativeBase):
    pass
class Todo(Base):
    __tablename__ = "todos"
    
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)

from sqlalchemy.orm import Session

with Session(engine) as session:
    new_todo = Todo(title= "Learn sqlalchemy")
    session.add(new_todo)
    session.commit()
    todos = session.query(Todo).all()
    for todo in todos:
        print(todo.id, todo.title)
    print("Todo added")
    print("Session opened")
    
