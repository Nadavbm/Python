from reader import app, db
from reader.models import Address

db.init_app(app)
db.create_all()
db.session.commit()
