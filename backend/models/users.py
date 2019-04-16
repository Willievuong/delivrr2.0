import sys
sys.path.insert(0, '../')

from main import db
# from sqlalchemy.dialects.postgresql import JSON

class Users(db.Model):
  __tablename__ = 'users'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String())

