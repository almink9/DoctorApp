from doc import app, db
from flask import render_template, redirect, url_for, flash, request
from doc.models import User, Patient
from doc.forms import LoginForm
from flask_login import login_user, logout_user, login_required, current_user

@app.route("/")
@app.route("/home")
def home_page():
  patient = Patient.query.all()
  return render_template('home.html', data=patient)
  
@app.route('/login', methods=['GET', 'POST'])
def login_page():
  form = LoginForm()
  if form.validate_on_submit():
    attempted_user = User.query.filter_by(email_address=form.email_address.data).first()
    if attempted_user and attempted_user.check_password_correction(attempted_password = form.password.data):
      login_user(attempted_user)
      flash(f'Success! You are logged in', category='success') 
      return redirect(url_for('home_page'))
    else:
      flash('Invalid email or password.', category='danger')
  return render_template('login.html', form=form)

@app.route('/logout')
def logout_page():
  logout_user()
  flash("You have been logged out.", category='info')
  return redirect(url_for('home_page'))