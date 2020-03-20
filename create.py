from application import db
from application.models import Activities, Users

db.drop_all()
db.create_all()