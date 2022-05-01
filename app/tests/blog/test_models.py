from app.extensions.database import db
from datetime import datetime
from app.blog.models import Blog


def test_blog_update(client):
    # update blog's properties
    blog = Blog(title='Test Blog',
                content='This is a test',
                picture_url='https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/Flask_logo.svg/1200px-Flask_logo.svg.png',
                date=datetime.date(datetime.utcnow()))
    db.session.add(blog)
    db.session.commit()

    blog.content = 'Update test content'
    blog.save()

    updated_blog = Blog.query.filter_by(title='Test Blog').first()
    assert updated_blog.content == 'Update test content'
