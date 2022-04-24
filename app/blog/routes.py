import imp
from flask import Blueprint, redirect, render_template, request, url_for, current_app
from .models import Blog
from app.users.models import User
from flask_login import login_required, current_user, user_accessed

blueprint = Blueprint('blog', __name__)

# Routes


@blueprint.route('/blogs')
def blogs():
    page_number = request.args.get('page', 1, type=int)
    blogs_pagination = Blog.query.paginate(
        page_number, current_app.config['POSTS_PER_PAGE'])
    return render_template('blog/blogs.html', blogs_pagination=blogs_pagination, page_number=page_number)


@blueprint.route('/blogs/<id>', methods=('GET', 'POST'))
def blog(id):
    blog = Blog.query.get(id)
    user = User.query.get(blog.user_id)

    if request.method == 'POST':
        blog.delete()
        return redirect(url_for('blog.blogs'))

    return render_template(
        'blog/blog.html',
        blog=blog,
        user=user
    )


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
        if not request.form.get('title'):
            raise Exception(
                'The blog post must have a title.')

        elif not request.form.get('content'):
            raise Exception(
                'The blog post must have some content.')
        new_post = Blog(
            title=request.form['title'],
            content=request.form['content'],
            picture_url=request.form['picture_url'],
            user_id=current_user.id)
        new_post.save()
        return redirect(url_for('blog.blogs'))

    except Exception as error_message:
        error = error_message or 'An error occurred while creating a post. Please make sure to enter valid data.'
        return render_template(
            'blog/new_blog.html',
            error=error
        )
