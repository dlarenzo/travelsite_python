from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from . import db ## means from __init__.py


auth = Blueprint('auth', __name__)

#define route and function for each of the login/ registration routes
@auth.route('/login')
def login():
  
  return render_template("login.html", text="Testing", )

@auth.route('/logout')
# Make sure page is only accessible to logged in users by using @login_required
@login_required
def logout():
  logout_user()
  return redirect(url_for('auth.login'))

@auth.route('/logout')
# Make sure page is only accessible to logged in users by using @login_required
@login_required
def logout():
  logout_user()
  return redirect(url_for('auth.login'))
  
@auth.route('/sign-up')
def sign_up():
  if request.method == 'POST':
    email = request.form.get('email')
    first_name = request.form.get('firstName')
    password1 = request.form.get('password1')
    password2= request.form.get('password2')
    
    # Does email already exist in database?
    user = User.query.filter_by(email=email).first()
    if user:
      flash("Email already exists", category='error')
      
    # Is email meets the criteria below?
    if len(email) < 4:
      flash("Email must be greater than 3 characters", category='error')
    elif len(first_name) < 2:
      flash("First name must be greater than 1 character", category='error')
    elif password1 != password2:
      flash("Passwords don't match", category='error')
    elif len(password1) < 7:
      flash('Password must be at least 7 characters', category='error')
    else:
      # Create new user for the database
      new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method='pbkdf2:sha256'))
      # Add new user to the database
      db.session.commit()
      # Log in the new user and remember user history until cleared
      login_user(new_user, remember=True)
      # Flash a message to the user that they have successfully signed up
      flash('Account created!', category='success')
      # Redirect user to the home page
    return render_template("sign_up.html", user=current_user)
  
@auth.route('/travel')
def travel():
  return render_template("travel.html")
  
@auth.route('/eat')
def eat():
  return render_template("eat.html")
  
@auth.route('/relax')
def relax():
  return render_template("relax.html")