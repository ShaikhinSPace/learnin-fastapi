from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum
from fastapi import HTTPException
app = FastAPI()

class Category(str,Enum):
    PERSONAL = 'personal'
    WORK = 'work'

class ToDo(BaseModel):
    title: str
    completed: bool
    id:int
    category: Category 
    
todos = {0: ToDo(title='test1',category=Category.WORK,completed='true',id='0'),
         1: ToDo(title='test2',category=Category.PERSONAL,completed='false',id='1')}


@app.get("/")
def index() -> dict:
    return {'todos':todos}

## Another way
#def index() -> dict[str, dict[int,ToDo]]:
#    return {'todos':todos}

@app.get('/todos/{todo_id}')
def get_todo_by_id(todo_id:int) -> ToDo:
    if todo_id not in todos:
        raise HTTPException(status_code=404,detail=f"{todo_id} does not exist")
    return todos[todo_id]

@app.get('/todos/')
def query_todo_by_completed(completed: bool | None=None) -> dict[str,list[ToDo]]:
    filtered_todos = [todo for todo in todos.values() if todo.completed is completed]
    return {'todos': filtered_todos}
    