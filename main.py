from typing import Optional
from fastapi import  FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
app = FastAPI() 
 

class Post(BaseModel):
    title :str
    content:str
    published:bool = False
    rating: Optional[int]=None
 

my_posts=[{"title": "title of post 1", "content": "content of post 1","id": 1},{
    "title": "favourite foods", "content": "I like pizza", "id": 2
}]

def find_post(id):
    for p in my_posts:
        if p['id']==id:
            return p
        
@app.get("/")
async def root():
    return {"message": "Hello !"}

# Read Operations
@app.get("/post")
def get_post():
    return {"data": my_posts}

# Create Operations
@app.post("/post", status_code=status.HTTP_201_CREATED)
def creat_post(new_post : Post):
    post_dict=new_post.dict()
    post_dict['id']=randrange(0,1000000000)
    my_posts.append(post_dict)
    return {"data": new_post}

# Read Operations by ID
@app.get('/post/id/{id}')
def get_post(id: int): 
    post= find_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No such post")
    return {"post_details": post}

# Latest post
@app.get('/post/latest')
def get_latest():
    post = my_posts[len(my_posts)-1]
    return {"post_details": post}
