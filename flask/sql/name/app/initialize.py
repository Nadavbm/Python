from named import app, db
from named.models import Name

db.init_app(app)
db.drop_all()
db.create_all()
db.session.commit()
