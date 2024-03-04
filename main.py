from fastapi import FastAPI 

app = FastAPI()


@app.get("/")
async def root():
  return{"message" : "welcome to the API!!"}
  
@app.get("/posts")
def get_post():
  return{"data" : "This is your posts"}
