from fastapi import FastAPI
from config import Base, engine
from models import *
from users.router import userRouter

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/")
def hello():
  return {"message": "Hello"}

app.include_router(userRouter)