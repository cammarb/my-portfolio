from app.app import create_app
from app.blog.models import Blog
from app.extensions.database import db

app = create_app()
app.app_context().push()

# Test for dynamic pages
blog_posts = {
    '1': {
        "title": "Blog 1",
        "content": "This is the description for Blog 1"
    },
    '2': {
        "title": "Blog 2",
        "content": "This is the description for Blog 2"
    },
    '3': {
        "title": "Blog 3",
        "content": "This is the description for Blog 3"
    },
}

for id, post in blog_posts.items():
    new_post = Blog(id=id, title=post['title'], content=post['content'])
    db.session.add(new_post)

db.session.commit()
