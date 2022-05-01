from app.extensions.database import db
from datetime import datetime
from app.projects.models import Project


def test_Project_update(client):
    # update Project's properties
    new_project = Project(title='Miley-API',
                          description='This is the description of my awesome project',
                          gh_link='https://github.com/cammarb/test',
                          image_link='https://m.media-amazon.com/images/I/71-DFlPOZSL._SL1046_.jpg')
    db.session.add(new_project)
    db.session.commit()

    new_project.gh_link = 'https://github.com/cammarb/miley-api'
    new_project.save()

    updated_project = Project.query.filter_by(title='Miley-API').first()
    assert updated_project.gh_link == 'https://github.com/cammarb/miley-api'
