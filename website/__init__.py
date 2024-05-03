from flask import Flask

def create_app():
  app = Flask(__name__)
  app.config['SECRET_KEY'] = 'asdf;lkj'
  
  # IMPORT THE VIEWS AND AUTH BLUEPRINTS HERE
  from .views import views
  from .auth import auth

  # NOW WE NEED TO REGISTER THE BLUEPRINTS
  app.register_blueprint(views, url_prefix='/')
  app.register_blueprint(auth, url_prefix='/')
  
  
  
  
  return app



