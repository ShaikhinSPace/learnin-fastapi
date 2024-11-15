from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum
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
#def index() -> dict[str, dict[int,ToDo]]:
#    return {'todos':todos}