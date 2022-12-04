from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import UserMixin

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///doc.db'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

class User(db.Model, UserMixin):
  id = db.Column(db.Integer(), primary_key=True)
  email_address = db.Column(db.String(length=30), nullable=False, unique=True)
  password_hash = db.Column(db.String(length=60), nullable=False)

  @property
  def password(self):
    return self.password

  @password.setter
  def password(self, plain_text_password):
    self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')


from doc import routes