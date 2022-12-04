from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///doc.db'
app.config['SECRET_KEY'] = '563ec91eee0d9950b2ce7972'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)


from doc import routes