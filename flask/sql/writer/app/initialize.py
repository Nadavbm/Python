from writer import app, db
from writer.models import Person

db.init_app(app)
db.create_all()
db.session.commit()
