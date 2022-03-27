from flask import Blueprint, render_template, request
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


@blueprint.route('/blogs/new', methods=('GET', 'POST'))
def new_blog():
    if request.method == 'POST':
        new_post = Blog(
            title=request.form['title'],
            content=request.form['content'],
            picture_url=request.form['picture_url']
        )
        new_post.save()
    return render_template(
        'new_blog.html'
    )
