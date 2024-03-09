from fastapi import FastAPI 
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Post(BaseModel):
  title: str
  content: str
  published :bool = True
  rating: Optional[int] = None
  


@app.get("/")
async def root():
  return{"message" : "welcome to the API!!"}
  
@app.get("/posts")
def get_post():
  return{"data" : "This is your posts"}


@app.post("/posts")
def create_posts(post:Post):
  print(post)
  print(post.dict())
  return {"data" : "post"}

