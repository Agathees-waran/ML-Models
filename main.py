from fastapi import FastAPI

app=FastAPI()

@app.get("/hello")
async def Hello():
    return "Hello Mapla"

list={1:"number one",
      2:"number two",
      3:"number three",
      4:"number Four",
      5:"number five"
}
@app.get("/number/6")
async def number():
    return "the number is 6"

@app.get("/number/{num:int}")
async def number(num):
    return list.get(num,"the number is not found try asgain")

from enum import Enum

class Books(str,Enum):
    Tamil="Tamil"
    English="English"
    Maths="Maths"
    Science="Science"
    Social="Social Science"

@app.get("/value/{name}")
async def sport(name:Books):
    if name == Books.Tamil:
        return Books.Tamil
    elif name is Books.English:
        return Books.English
    elif name is Books.Maths:
        return Books.Maths
    elif name is Books.Science:
        return Books.Science
    elif name is Books.Social:
        return Books.Social
    else:
        return "Not Found"
s=[s for s in Books]

@app.get("/one")
async def one():
    return s
class number(int,Enum):
    one=1
    two=2
    three=3
    four=4
    five=5
@app.get("/add/{num1}/{num2}")
async def add(num1:number,num2:number):
    return num1+num2

@app.get("/files/{file_path:path}")
async def read_file(file_path:str):
    return {"file_path":file_path}

fake=[{"i":"f"},{"i":"g"},{"i":"h"}]

@app.get("/items/")
async def read_item(sky:int=0,limit:int=10):
    return fake[sky:sky+limit]

@app.get("/sum/")
async def sum(short:bool=False,need:str="hi",get:str|None=None,):
    if short:
        return f"{2*5}+{need}"
    elif get:
        return get+need
    else:
        return f"{2+5}+{need}"
    
from pydantic import BaseModel

class Items(BaseModel):
    name:str
    desceiption:str|None=None
    price:str
    tax:float|None=None

@app.post("/item/")
async def create_item(item:Items):
    item_dict=item.dict()
    if item.tax is not None:
        price_with_tax=item.price+item.tax
        item_dict.update({"price_with_tax":price_with_tax})
    return item


    