import os 
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from app import app, db

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models.Account import Account

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
  manager.run()
  
  