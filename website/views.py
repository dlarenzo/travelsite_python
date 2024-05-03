from flask import Blueprint, render_template

views = Blueprint('views', __name__)

#---------------------- DEFINE A VIEW ----------------------#
@ views.route('/')
def home():
  return "<h1>Test Home</h1>"