from app.blog.models import Blog
from datetime import datetime


def test_blog_renders_blog(client):
    # Page loads and renders blog posts
    new_post = Blog(title='Test Blog',
                    content='This is a test',
                    picture_url='https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/Flask_logo.svg/1200px-Flask_logo.svg.png',
                    date=datetime.date(datetime.utcnow()))
    new_post.save()

    response = client.get('/blogs')

    assert b'Test Blog' in response.data
