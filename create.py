from application import db
from application.models import Activity, Activities, Users

db.drop_all()
db.create_all()