from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import JSON
# from app import db 

Base = declarative_base()

class Account(Base):
    __tablename__ = 'account'
    id = Column(Integer, primary_key=True)
    fb_id = Column(Integer)
    firstname = Column(String())
    lastname = Column(String())
    age = Column(Integer)

    # Constructor Method
    def __init__(self, id, firstName, lastName, age): 
      self.id = id
      self.firstname = firstName
      self.lastname = lastName
      self.age = age 

    # Query Method 
    def __repr__(self):
      return '<id {}>'.format(self.id)

# CREATE TABLE Account(id int, fb_id int, firstName varchar(255), lastName varchar(255), age int);