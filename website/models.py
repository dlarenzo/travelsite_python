from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):
  # define all the columns in the Schema
  id = db.Column(db.Integer, primary_key=True)
  # this is the title of the note
  data = db.Column(db.String(10000))
  date = db.Column(db.DateTime(timezone=True), default=func.now())
  # this is the user_id that is associated with the note.  This column references the user table and the id of another database.  We must pass a valid user id to this column to access the note
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
  


# User Schema
class User(db.Model, UserMixin):
  # define all the columns in the Schema
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(150), unique=True)
  password = db.Column(db.String(150))
  first_name = db.Column(db.String(150))
  # set up a relationship between the user and the notes.  This will allow us to access all the notes associated with a user.  Remember we built a Note Schema above.
  notes = db.relationship('Note')
  
# above is the completed setup of a database model for each column in the database