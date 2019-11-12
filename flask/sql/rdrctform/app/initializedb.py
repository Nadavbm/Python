from redirect.models import User
from redirect import db, app

db.init_app(app)
db.create_all()
db.session.commit()

