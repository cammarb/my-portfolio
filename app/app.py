import os
from flask import Flask, render_template
from app.extensions.database import db, migrate

from . import simple_pages
from . import projects
from . import blog
from . import users


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config')

    register_extensions(app)
    register_blueprints(app)

    return app


def register_blueprints(app: Flask):
    app.register_blueprint(projects.routes.blueprint)
    app.register_blueprint(blog.routes.blueprint)
    app.register_blueprint(simple_pages.routes.blueprint)
    app.register_blueprint(users.routes.blueprint)


def register_extensions(app: Flask):
    db.init_app(app)
    migrate.init_app(app, db)
