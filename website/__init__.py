from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

# Telling flask how we login and logout users
from flask_login import LoginManager

# Define the database and give it a name 
db=SQLAlchemy()
DB_NAME = "database.db"

def create_app():
  # init flask app
  app = Flask(__name__)
  app.config['SECRET_KEY'] = 'asdf;lkj'
  app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
  db.init_app(app)
  
  # IMPORT THE VIEWS AND AUTH BLUEPRINTS HERE
  from .views import views
  from .auth import auth

  # NOW WE NEED TO REGISTER THE BLUEPRINTS
  app.register_blueprint(views, url_prefix='/')
  app.register_blueprint(auth, url_prefix='/')
  
  # ---------------------- DATABASE CHECK  ----------------------#  
  from .models import User
  
  create_database(app)
  
  login_manager = LoginManager()
  login_manager.login_view = 'auth.login'
  login_manager.init_app(app)
  
  # ----------- USER LOADER FUNCTION -----------#
  @login_manager.user_loader
  def load_user(id):
    return User.query.get(int(id))
  
  return app

#Function checks if there is a database and if not creates one
  
def create_database(app):
  if not path.exists('website/' + DB_NAME):
    with app.app_context():
      db.create_all()
    print('Created Database!')
      



