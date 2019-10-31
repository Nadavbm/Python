from named import app, db
from named.models import Name

name1 = Name(name='Nadav')
name2 = Name(name='ButholeSurfers')
name3 = Name(name='Steven')
name4 = Name(name='Hairway')

db.session.add(name1)
db.session.add(name2)
db.session.add(name3)
db.session.add(name4)

db.session.commit()


