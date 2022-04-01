from flask import Blueprint, redirect, render_template, request, url_for
from .models import Project
from flask_login import login_required

blueprint = Blueprint('projects', __name__)

# Routes


@blueprint.route('/projects')
def projects():
    all_projects = Project.query.all()
    return render_template('projects/projects.html', projects=all_projects)


@blueprint.route('/projects/<id>', methods=('GET', 'POST'))
def project(id):
    project = Project.query.get(id)
    if request.method == 'POST':
        project.delete()
        return redirect(url_for('projects.projects'))

    return render_template(
        'projects/project.html',
        project=project
    )


@blueprint.route('/projects/new', methods=('GET', 'POST'))
@login_required
def new_project():
    if request.method == 'POST':
        new_project = Project(
            title=request.form['title'],
            description=request.form['description'],
            gh_link=request.form['gh_link'],
            image_link=request.form['image_link'],
        )
        new_project.save()
        return redirect(url_for('projects.project', id=new_project.id))

    return render_template(
        'projects/new_project.html',
        project=project
    )
