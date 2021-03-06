from .models import Blog


def save_post(req_form, user):
    if not req_form.get('title'):
        raise Exception(
            'The blog post must have a title.')

    elif not req_form.get('content'):
        raise Exception(
            'The blog post must have some content.')
    new_post = Blog(
        title=req_form['title'],
        content=req_form['content'],
        picture_url=req_form['picture_url'],
        user_id=user.id)
    new_post.save()
    return new_post.id


def update_post(req_form, current_blog):
    if not req_form.get('title'):
        raise Exception(
            'The blog post must have a title.')

    elif not req_form.get('content'):
        raise Exception(
            'The blog post must have some content.')
    current_blog.title = req_form['title']
    current_blog.content = req_form['content']
    current_blog.picture_url = req_form['picture_url']
    current_blog.save()
