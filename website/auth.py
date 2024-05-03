from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)

#define route and function for each of the login/ registration routes
@auth.route('/login')
def login():
    return "<p>Login</p>"

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"
  
@auth.route('/sign-up')
def sign_up():
    return "<p>Sign-up</p>"
  
@auth.route('/travel')
def travel():
    return "<p>Travel</p>"
  
@auth.route('/eat')
def eat():
    return "<p>Eat</p>"
  
@auth.route('/relax')
def relax():
    return "<p>Relax</p>"