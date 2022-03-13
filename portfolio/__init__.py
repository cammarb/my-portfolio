import os
from flask import Flask, render_template

# Test for dynamic pages
projects = {
    '1': {
        "name": "Project 1",
        "description": "This is the description for Project 1"
    },
    '2': {
        "name": "Project 3",
        "description": "This is the description for Project 2"
    },
    '3': {
        "name": "Project 3",
        "description": "This is the description for Project 3"
    },
}


def create_app():
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Routes
    @ app.route('/')
    def home():
        return render_template('home.html')

    @ app.route('/projects')
    def list_projects():
        return render_template('projects.html')

    @ app.route('/projects/<id>')
    def get_project(id):
        name = projects[id]["name"]
        description = projects[id]["description"]

        return render_template(
            'project.html',
            name=name,
            description=description
        )

    @ app.route('/contact')
    def contact():
        return render_template('contact.html')

    return app
