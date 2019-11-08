from address import app, db
from address.models import Address

db.init_app(app)
db.create_all()
db.session.commit()
