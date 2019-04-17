import sys
from app import db
from sqlalchemy.dialects.postgresql import JSON
sys.path.insert(0, '../')

class Users(db.Model):
  __tablename__ = 'users'

  id = db.Column(db.Integer, primary_key=True)
  firstName = db.Column(db.String())
  lastName = db.Column(db.String())
  age = db.Column(db.Integer)

  #Constructor Method
  def __init__(self, firstName, lastName, age): 
    self.firstName = firstName
    self.lastName = lastName
    self.age = age; 

  #Query Method 
  def __repr__(self):
    return '<id {}>'.format(self.id)

