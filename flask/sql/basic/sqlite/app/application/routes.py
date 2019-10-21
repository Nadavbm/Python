from flask import request, render_template, make_response
from datetime import datetime
from flask import current_app as app
from .models import db, User

@app.route('/', methods=['GET'])
def create_user():
	username = request.args.get('user')
	email = request.args.get('email')
	if username and email:
		new_user = User(username=username, email=email,reated=datetiem.now(),)
		db.session.add(new_user)
		db.session.commit()
	return make_response(f"{new_user} created!")



