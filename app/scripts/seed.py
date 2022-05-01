from app.app import create_app
from app.blog.models import Blog
from app.projects.models import Project
from datetime import datetime

from app.extensions.database import db

app = create_app()
app.app_context().push()

# Projects
projects = {
    '1': {
        "title": "My portfolio",
        "description": "💻 Website containing all full-stack development projects, as well as blog posts.",
        "gh_link": "https://github.com/cammarb/my-portfolio.git",
        "image_link": "https://raw.githubusercontent.com/cammarb/my-portfolio/master/portfolio-screenshot.jpg"
    },
    '2': {
        "title": "Yugi Decks",
        "description": "Yu-Gi-Oh library using Yu-Gi-Oh's API",
        "gh_link": "https://github.com/cammarb/yugi-decks.git",
        "image_link": "https://raw.githubusercontent.com/cammarb/yugi-decks/master/screenshot.png"
    },
    '3': {
        "title": "Miley API",
        "description": "The Miley Cyrus API is based on Miley Cyrus's music carreer. You will have access to data about all of her released albums and songs (Movies and TV Shows soon to be added).",
        "gh_link": "https://github.com/cammarb/miley-api",
        "image_link": "https://i.redd.it/spc04jy1jvx61.png"
    }
}

for id, project in projects.items():
    new_project = Project(
        title=project['title'],
        description=project['description'],
        gh_link=project['gh_link'],
        image_link=project['image_link'])
    db.session.add(new_project)

db.session.commit()


# Blog
blog_posts = {
    '1': {
        "title": "Learning Flask",
        "content": "I am currently taking a course called 'Foundations of Web development' which required me to use Flask (Python microframework) to learn the basics of...well Web Development. What I am loving most about Flask is it's simplicity. It is also really lightweight and because you basically start from scratch and install just the tools you could need. It's been quite easy to learn Flask, and I believe all this learned knowledge will make it even easier for me to learn Django, which is a more popular Python framework, and it's on the top ten of most in-demand technologies for web programming this year.",
        "picture_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/Flask_logo.svg/1200px-Flask_logo.svg.png",
        "date": datetime.date(datetime.utcnow()),
        "user_id": 1
    }
}

for id, post in blog_posts.items():
    new_post = Blog(

        title=post['title'],
        content=post['content'],
        picture_url=post['picture_url'],
        date=post['date'],
        user_id=post['user_id'])
    db.session.add(new_post)

db.session.commit()
