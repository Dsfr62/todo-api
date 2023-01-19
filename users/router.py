from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from config import get_db
from users.service import UserService
from dto import RegisterUser

userRouter = APIRouter(prefix="/users", tags=["Users"])

@userRouter.get("/", status_code=status.HTTP_200_OK)
async def getAllUser(db:Session=Depends(get_db)):
    return UserService.get_allUser(db=db)

@userRouter.get("/{id}", status_code=status.HTTP_200_OK)
async def getUser(id: int, db:Session=Depends(get_db)):
    return UserService.get_user(id, db)

@userRouter.post("/", status_code=status.HTTP_201_CREATED)
async def createUser(user: RegisterUser, db:Session=Depends(get_db)):
    return UserService.create_user(user, db)

@userRouter.delete("/{id}", status_code=status.HTTP_200_OK)
async def deleteUser(id: int, db:Session=Depends(get_db)):
    return UserService.delete_user(id, db)