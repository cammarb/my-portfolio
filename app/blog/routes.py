import imp
from flask import Blueprint, redirect, render_template, request, url_for, current_app
from .models import Blog
from .services import *
from app.users.models import User
from flask_login import login_required, current_user

blueprint = Blueprint('blogs', __name__)

# Routes


@blueprint.route('/blogs')
def blogs():
    page_number = request.args.get('page', 1, type=int)
    blogs_pagination = Blog.query.paginate(
        page_number, current_app.config['POSTS_PER_PAGE'])
    return render_template('blog/blogs.html', blogs_pagination=blogs_pagination, page_number=page_number)


@blueprint.get('/blogs/<int:id>')
def get_blog(id):
    blog = Blog.query.get(id)
    user = User.query.get(blog.user_id)

    return render_template(
        'blog/blog.html',
        blog=blog,
        user=user
    )


@blueprint.post('/blogs/<int:id>')
def delete_blog(id):
    blog = Blog.query.get(id)
    blog.delete()
    return redirect(url_for('blogs.blogs'))

# Edit current blog post


@blueprint.get('/blogs/<int:id>/edit')
def get_edit_blog(id):
    blog = Blog.query.get(id)
    return render_template('blog/edit_blog.html', blog=blog)


@blueprint.post('/blogs/<int:id>/edit')
def edit_blog(id):
    blog = Blog.query.get(id)
    update_post(request.form, blog)
    return redirect(url_for('blogs.get_blog', id=blog.id))


@blueprint.get('/blogs/new')
@login_required
def get_blogs():
    return render_template(
        'blog/new_blog.html',
    )


@blueprint.post('/blogs/new')
@login_required
def new_blog():
    try:
        blog_id = save_post(request.form, current_user)
        blog_id
        return redirect(url_for('blogs.get_blog', id=blog_id))

    except Exception as error_message:
        error = error_message or 'An error occurred while creating a post. Please make sure to enter valid data.'
        return render_template(
            'blog/new_blog.html',
            error=error
        )
