#!/usr/bin/env python3
""" SQLAlchemy user model """

from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False, unique=True)
    hashed_password = Column(String(250), nullable=False)
    is_active = Column(Boolean, default=True)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)

