from flask import Blueprint, render_template

blueprint = Blueprint('portfolio', __name__)

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

# Routes


@blueprint.route('/projects')
def list_projects():
    return render_template('projects.html')


@blueprint.route('/projects/<id>')
def get_project(id):
    name = projects[id]["name"]
    description = projects[id]["description"]

    return render_template(
        'project.html',
        name=name,
        description=description
    )
