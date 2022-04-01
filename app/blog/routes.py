from flask import Blueprint, redirect, render_template, request, url_for
from .models import Blog
from flask_login import login_required

blueprint = Blueprint('blog', __name__)

# Routes


@blueprint.route('/blogs')
def blogs():
    all_blogs = Blog.query.all()
    return render_template('blog/blogs.html', blogs=all_blogs)


@blueprint.route('/blogs/<id>', methods=('GET', 'POST'))
def blog(id):
    blog = Blog.query.get(id)

    if request.method == 'POST':
        blog.delete()
        return redirect(url_for('blog.blogs'))

    return render_template(
        'blog/blog.html',
        blog=blog
    )


@blueprint.route('/blogs/new', methods=('GET', 'POST'))
@login_required
def new_blog():
    if request.method == 'POST':
        new_post = Blog(
            title=request.form['title'],
            content=request.form['content'],
            picture_url=request.form['picture_url']
        )
        new_post.save()
        return redirect(url_for('blog.blog', id=new_post.id))

    return render_template(
        'blog/new_blog.html',
    )
