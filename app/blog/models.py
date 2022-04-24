from email.policy import default
from app.extensions.database import db, CRUDMixin
from datetime import datetime


class Blog(db.Model, CRUDMixin):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    content = db.Column(db.String(800))
    picture_url = db.Column(db.String(200))
    date = db.Column(db.Date, nullable=False,
                     default=datetime.date(datetime.utcnow()))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
