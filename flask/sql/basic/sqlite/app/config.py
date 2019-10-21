from os import environ

class Config:
	# General config
	TESTING = environ["TESTING"]
	FLASK_DEBUG = environ["FLASK_DEBUG"]
	SECRET_KEY = environ.get('SECRET_KEY')
	# DB config
	SQLALCHEMY_DATABASE_URI = environ.get("SQLALCHEMY_DATABASE_URI")
	SQLALCHEMY_TRACK_MODIFICATIONS = environ.get("SQLALCHEMY_TRACK_MODIFICATIONS")

