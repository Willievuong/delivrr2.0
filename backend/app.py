from flask import Flask
from models.Model import db
from models import Account
import os

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

user = Account(firstName="Will", lastName="Vuong", age="12")

# @app.route('/')
# def userAcc()
#   return "Hello World!"
 
  
# if __name__ == '__main__':
#   app.run()

