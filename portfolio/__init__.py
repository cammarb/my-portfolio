import os
from flask import Flask, render_template


def create_app():
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Routes
    @app.route('/')
    def home():
        return render_template('home.html')

    @app.route('/projects')
    def list_projects():
        return render_template('projects.html')

    @app.route('/contact')
    def contact():
        return render_template('contact.html')

    return app
