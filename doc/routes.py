from doc import app
from flask import render_template, redirect, url_for, flash, request 
from doc.models import User
from doc.forms import LoginForm
from flask_login import login_user, logout_user, login_required, current_user

@app.route("/")
@app.route("/home")
def home_page():
  return render_template('home.html')
  
@app.route('/login', methods=['GET', 'POST'])
def login_page():
  form = LoginForm()
  return render_template('login.html', form=form)
