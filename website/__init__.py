from flask import Flask
from .admin import admin
from .views import views
from .auth import auth

def create_app():
  app = Flask(__name__)
  app.config['SECRET_KEY'] = 'rtfgyhunjmklkmjnhbgvfcdxszsexdrcftvgybhnjmk'
  
  app.register_blueprint(views, url_prefix='/')
  app.register_blueprint(auth, url_prefix='/auth')
  app.register_blueprint(admin, url_prefix='/admin')
  
  return app
