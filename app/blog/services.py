from .models import Blog


def create_post(req_form, user):
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
