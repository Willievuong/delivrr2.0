from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Account
import os

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# an Engine, which the Session will use for connection
# resources
some_engine = create_engine(os.environ['DATABASE_URL'])

# create a configured "Session" class
Session = sessionmaker(bind=some_engine)
session = Session()

# db = SQLAlchemy()

# def createApp(app):
#   db.init_app(app)
#   return app 

@app.route('/')
def userAcc():
  user = Account.Account(id = 2, firstName="Robert", lastName="Chen", age="12")
  # db.session.add(user) 
  # db.session.commit()
  session.add(user) 
  session.commit()
  
  return user.firstname
 
  
if __name__ == '__main__':
  # app = createApp(app)
  app.run()

