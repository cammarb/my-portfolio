from email.policy import default
from app.extensions.database import db, CRUDMixin
from datetime import datetime


class UserPost(db.Model):
    post_id = db.Column(db.Integer, db.ForeignKey("blog.id"), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), primary_key=True)


class Blog(db.Model, CRUDMixin):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    content = db.Column(db.String(800))
    picture_url = db.Column(db.String(200))
    date = db.Column(db.Date, nullable=False,
                     default=datetime.date(datetime.utcnow()))
    blog_user = db.relationship("User", secondary="user_post",
                                backref="user_post", lazy=True)
