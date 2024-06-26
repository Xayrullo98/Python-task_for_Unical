from sqlalchemy import Column, Integer, String, Boolean, Float, Text
from sqlalchemy.orm import relationship

from db import Base


class Users(Base):
    __tablename__ = "Users"
    id = Column(Integer, primary_key=True)
    roll = Column(String(20), nullable=True)
    name = Column(String(30), nullable=False)
    number = Column(String(30), nullable=True)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(200), nullable=False)
    active = Column(Boolean,default=True, nullable=True)
    status = Column(Boolean, nullable=False, default=True)
    token = Column(String(400), default='', nullable=True)
