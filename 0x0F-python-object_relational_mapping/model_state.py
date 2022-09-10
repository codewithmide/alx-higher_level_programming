#!/usr/bin/python3
"""
A python file that contains the class definition of a State and an instance Base = declarative_base():
"""
import sqlalchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name =  Column(String(128), nullable=False)

Base.metadata.create_all(engine)
