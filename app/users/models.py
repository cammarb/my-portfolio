from app.extensions.database import db, CRUDMixin
from flask_login import UserMixin


class User(db.Model, CRUDMixin, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    name = db.Column(db.String(100))
    passwd = db.Column(db.String(300))
    blogs = db.relationship("Blog", backref="user", lazy=True)
