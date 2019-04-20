from Model import db

class Account(db.Model):
  fbId = db.Column(db.Integer)
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
