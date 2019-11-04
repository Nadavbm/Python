from writer import app, db
from writer.models import Address

address1 = Address(name='nadav',street='buffstr',number=12,city='Tel Aviv',country='Israel')
address2 = Address(name='tzili',street='ezrastr',number=32,city='New York',country='US')
address3 = Address(name='gili',street='hummusstr',number=14,city='Frakfurt',country='Germany')
address4 = Address(name='yeruham',street='somewherestr',number=78,city='Yeruham',country='Israel')
address5 = Address(name='bezalel',street='kebabstr',number=99,city='Tel Aviv',country='Israel')

db.session.add(address1)
db.session.add(address2)
db.session.add(address3)
db.session.add(address4)
db.session.add(address5)

db.session.commit()

