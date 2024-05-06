
from flask_login import UserMixin
from sqlalchemy.sql import func

# User Schema
# class User(db.Model, UserMixin):
#   # define all the columns in the Schema
#   id = db.Column(db.Integer, primary_key=True)
#   email = db.Column(db.String(150), unique=True)
#   password = db.Column(db.String(150))
#   first_name = db.Column(db.String(150))
#   # set up a relationship between the user and the notes.  This will allow us to access all the notes associated with a user.  Remember we built a Note Schema above.
#   notes = db.relationship('Note')