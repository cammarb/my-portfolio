from flask import Blueprint, render_template
from .models import Blog

blueprint = Blueprint('blog', __name__)

# Routes


@blueprint.route('/blogs')
def blogs():
    all_blogs = Blog.query.all()
    return render_template('blogs.html', blogs=all_blogs)


@blueprint.route('/blogs/<id>')
def blog(id):
    blog = Blog.query.get(id)

    return render_template(
        'blog.html',
        blog=blog
    )


@blueprint.route('/blogs/new')
def new_blog():

    return render_template(
        'new_blog.html'
    )
