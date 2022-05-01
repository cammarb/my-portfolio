from app.blog.models import Blog
from app.users.models import User
from datetime import datetime


def test_blog_renders_blog(client):
    # Page loads and renders blog posts
    new_post = Blog(title='Test Blog',
                    content='This is a test',
                    picture_url='https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/Flask_logo.svg/1200px-Flask_logo.svg.png',
                    date=datetime.date(datetime.utcnow()),
                    user_id=1)
    new_post.save()

    response = client.get('/blogs')

    assert b'Test Blog' in response.data


# def test_post_user_blog(client):
#     # Creates a blog related to the user
#     response = client.post('/blogs/new', data={
#         "id": 1,
#     })
#     assert User.query.get(1) is 1
