import email
from app.extensions.database import db, CRUDMixin


class User(db.Model, CRUDMixin):
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    name = db.Column(db.String(100))
