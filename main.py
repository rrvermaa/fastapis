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
        

def find_index_post(id):
    for i,p in enumerate(my_posts):
        if p['id']==id:
            return i
        
        

        
 #http method       # path
@app.get("/") # decorator have app which contain fastapi instance 
async def root(): # async is not necessary
    return {"message": "Hello !"}

# Read Operations
@app.get("/post")
def get_post():
    return {"data": my_posts}

# Create Operations
@app.post("/post", status_code=status.HTTP_201_CREATED)
def creat_post(new_post : Post):
    post_dict=new_post.dict()
    post_dict['id']=randrange(0,1000000000) # give unique id
    my_posts.append(post_dict)
    return {"data": new_post}



# Latest post
@app.get('/post/latest')   
def get_latest():
    post = my_posts[len(my_posts)-1]
    return {"post_details": post}


# Read Operations by ID
@app.get('/post/{id}')
def get_post(id: int): #convert id into an integer
# def get_post(id: int,response: Response):
    post= find_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No such post")
    return {"post_details": post}


"""here is an issue that when we are going to post/latest then it took latest as id and run get_post 
solution is that I have to get_latest function before get_post function....
"""

@app.delete('/posts/{id}',status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int):
    #delete post
    #find the index in the array that has required ID
    #my post_index id              
    index=find_index_post(id)
    if index ==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='post not found')
    my_posts.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put('/posts/{id}')
def update_post(id:int,post:Post):
    index=find_index_post(id)
    if index ==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='post not found')
    
    post_disc=post.dict()
    post_disc['id']=id
    my_posts[index]=post_disc
    return {'message':post_disc }