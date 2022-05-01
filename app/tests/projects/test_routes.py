from app.projects.models import Project
from datetime import datetime


def test_project_renders_project(client):
    # Page loads and renders project posts
    new_post = Project(title='Miley-API',
                       description='This is the description of my awesome project',
                       gh_link='https://github.com/cammarb/miley-api',
                       image_link='https://m.media-amazon.com/images/I/71-DFlPOZSL._SL1046_.jpg')
    new_post.save()

    response = client.get('/projects')

    assert b'Miley-API' in response.data
