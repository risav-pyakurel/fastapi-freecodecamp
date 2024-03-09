from fastapi import FastAPI 
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()

class post(BaseModel):
  title: str
  content: str


@app.get("/")
async def root():
  return{"message" : "welcome to the API!!"}
  
@app.get("/posts")
def get_post():
  return{"data" : "This is your posts"}


@app.post("/createposts")
def create_posts(new_post:post):
  print(new_post.title)
  return {"data" : "newpost"}

