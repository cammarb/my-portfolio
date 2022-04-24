from app.projects.models import Project


def create_project(req_form):
    new_project = Project(
        title=req_form['title'],
        description=req_form['description'],
        gh_link=req_form['gh_link'],
        image_link=req_form['image_link'],
    )
    new_project.save()
