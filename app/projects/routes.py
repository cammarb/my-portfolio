from flask import Blueprint, redirect, render_template, request, url_for
from .models import Project
from .services import *
from flask_login import login_required

blueprint = Blueprint('projects', __name__)

# Routes


@blueprint.route('/projects')
def projects():
    all_projects = Project.query.all()
    return render_template('projects/projects.html', projects=all_projects)


@blueprint.get('/projects/<id>/edit')
@login_required
def get_project(id):
    project = Project.query.get(id)
    return render_template(
        'projects/project.html',
        project=project
    )


@blueprint.post('/projects/<int:id>/edit')
@login_required
def update_project(id):
    project = Project.query.get(id)
    update(request.form, project)
    return redirect(url_for('projects.projects'))


@blueprint.post('/projects/<int:id>')
@login_required
def delete_project(id):
    project = Project.query.get(id)
    project.delete()
    return redirect(url_for('projects.projects'))


@blueprint.get('/projects/new')
@login_required
def new_project():
    return render_template(
        'projects/new_project.html'
    )


@blueprint.post('/projects/new')
@login_required
def post_project():
    create_project(request.form)
    return redirect(url_for('projects.projects'))
