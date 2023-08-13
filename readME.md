run :
    uvicorn main:app --reload
    
sudo lsof -t -i tcp:8000 | xargs kill -9