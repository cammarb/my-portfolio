from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()


class CRUDMixin():
    def save(self):
        db.session.add(self)
        db.session.commit(self)
        return self

    def delete(self):
        db.session.delete(self)
        db.session.commit(self)
        return
