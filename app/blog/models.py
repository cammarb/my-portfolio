from app.extensions.database import db, CRUDMixin


class Blog(db.Model, CRUDMixin):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    content = db.Column(db.String(300))
    picture_url = db.Column(db.String(200))
