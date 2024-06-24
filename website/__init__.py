from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from .admin import admin
from .views import views
from .auth import auth

db = SQLAlchemy()
DB_NAME = 'database.sqlite3'

def create_database():
  db.create_all()
  print("Database Created")

def create_app():
  app = Flask(__name__)
  app.config['SECRET_KEY'] = 'rtfgyhunjmklkmjnhbgvfcdxszsexdrcftvgybhnjmk'
  app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
  
  db.init_app(app)
  
  app.register_blueprint(views, url_prefix='/')
  app.register_blueprint(auth, url_prefix='/auth')
  app.register_blueprint(admin, url_prefix='/admin')
  
  with app.app_context():
    create_database()
  
  return app
