from fastapi import  FastAPI
from fastapi.params import Body
from pydantic import BaseModel
app = FastAPI() 
 

class Post(BaseModel):
    title :str
    content:str
 
@app.get("/")
async def root():
    return {"message": "Hello !"}


@app.get("/post")
def get_post():
    return {"data": "New post!"}

@app.post("/createpost")
def creat_post(new_post : Post):
    print(new_post.title)
    return {"data": "new post!"}

#title string, content string
