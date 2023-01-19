from sqlalchemy import Column, Integer, Boolean, String, ForeignKey
from sqlalchemy.orm import relationship
from config import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    name = Column(String(64), nullable=False)
    email = Column(String(256), nullable=False, unique=True)
    password = Column(String(512), nullable=False)
    tasks = relationship("Task", back_populates="user")

    def __repr__(self):
        return f"<User name={self.name} email={self.email}"


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    activity = Column(String(256))
    is_done = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="tasks")

    def __repr__(self):
        return f"<Task activity={self.activity} is_done={self.is_done}"

