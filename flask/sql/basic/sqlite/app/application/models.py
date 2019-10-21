
from . import db

class User (db.Model):
	tablename = 'users'
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80), unique=True, nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)
	created = db.Column(db.DateTime, index=False, unique=False, nullable=False)

	def __repr__(self):
		return '<User {}>'.format(self.username)



