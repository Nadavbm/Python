from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
	app = Flask(__name__)
	db.init_app(app)
	TESTING = True
	DEBUG = True
	SECRET_KEY = '$3cR3t'
	SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
	SQLALCHEMY_TRACK_MODIFICATIONS = False

	#app.config.from_object('config.Config')

	with app.app_context():
		from . import routes

		db.create_all()

		return app

