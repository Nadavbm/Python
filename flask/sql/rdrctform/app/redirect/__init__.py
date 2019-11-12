from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'SomeSecret'
app.config['WTF_CSRF_KEY'] = 'SomeSecret'
app.config['WTF_CSRF_ENABLED'] = False
app.config['SQLALCHEMY_ECHO'] = True 

db = SQLAlchemy(app) 

from redirect import routes

