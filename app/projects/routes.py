from flask import Blueprint, render_template
from .models import Project

blueprint = Blueprint('projects', __name__)

# Routes


@blueprint.route('/projects', methods=['POST', 'GET'])
def projects():
    all_projects = Project.query.all()
    return render_template('projects.html', projects=all_projects)


@blueprint.route('/projects/<id>')
def project(id):
    project = Project.query.get(id)

    return render_template(
        'project.html',
        project=project
    )
