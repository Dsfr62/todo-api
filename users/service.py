from fastapi import Depends
from config import get_db
from sqlalchemy.orm import Session
from models import User
from dto import RegisterUser
from werkzeug.security import generate_password_hash

class UserService:
    def get_allUser(db: Session):
        return db.query(User).all()

    def get_user(id: int, db: Session = Depends(get_db)):
        user: User = db.query(User).filter(User.id == id).first()
        return {"name": user.name, "email": user.email, "tasks": user.tasks}

    def create_user(user: RegisterUser, db: Session = Depends(get_db)):
        new_user = User(
            name = user.name,
            email = user.email,
            password = generate_password_hash(user.password)
        )

        db.add(new_user)
        db.commit()

        db.refresh(new_user)
        new_user.password = None
        return new_user

    def delete_user(id: int, db: Session):
        user = db.query(User).filter(User.id == id).first()
        db.delete(user)
        db.commit()

        return user