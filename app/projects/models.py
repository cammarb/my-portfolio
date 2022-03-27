from app.extensions.database import db, CRUDMixin


class Project(db.Model, CRUDMixin):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.String(300))
    gh_link = db.Column(db.String(200))
    image_link = db.Column(db.String(200))
