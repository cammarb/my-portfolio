from app.app import create_app
from app.blog.models import Blog
from app.projects.models import Project
from app.extensions.database import db

app = create_app()
app.app_context().push()

# Projects
projects = {
    '1': {
        "name": "My portfolio",
        "description": "Portfolio website made with Python & Flask",
        "github": "https://github.com/cammarb/my-portfolio.git",
        "image": "https://raw.githubusercontent.com/cammarb/my-portfolio/master/portfolio_screenshot.png"
    },
    '2': {
        "name": "Yugi Decks",
        "description": "Yu-Gi-Oh library using Yu-Gi-Oh's API",
        "github": "https://github.com/cammarb/yugi-decks.git",
        "image": "https://raw.githubusercontent.com/cammarb/yugi-decks/master/screenshot.png"
    }
}

for id, project in projects.items():
    new_project = Project(
        id=id, title=project['name'],
        description=project['description'],
        gh_link=project['github'],
        image_link=project['image'])
    db.session.add(new_project)

db.session.commit()


# Blog
blog_posts = {
    '1': {
        "title": "Learning Flask development",
        "content": "This is the content for Blog 1"
    },
    '2': {
        "title": "How to install Ubuntu 22.04 LTS",
        "content": "This is the content for Blog 2"
    },
    '3': {
        "title": "Learning GTK4 for GNOME development",
        "content": "This is the content for Blog 3"
    },
}

for id, post in blog_posts.items():
    new_post = Blog(id=id, title=post['title'], content=post['content'])
    db.session.add(new_post)

db.session.commit()
