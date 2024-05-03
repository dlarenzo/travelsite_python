from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)

#define route and function for each of the login/ registration routes
@auth.route('/login')
def login():
    return render_template("login.html", text="Testing")

@auth.route('/logout')
def logout():
    return render_template("logout.html")
  
@auth.route('/sign-up')
def sign_up():
    return render_template("sign_up.html")
  
@auth.route('/travel')
def travel():
    return render_template("travel.html")
  
@auth.route('/eat')
def eat():
    return render_template("eat.html")
  
@auth.route('/relax')
def relax():
    return render_template("relax.html")