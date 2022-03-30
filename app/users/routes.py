from .models import User
from flask import Blueprint, render_template, request, url_for
from werkzeug.security import generate_password_hash, check_password_hash

blueprint = Blueprint('users', __name__)


@blueprint.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        new_user = User(
            name=request.form['name'],
            username=request.form['username'],
            password=request.form['password']
        )
        new_user.save()
        return render_template(url_for('users.login'))
    return render_template('users/register.html')


# @blueprint.route('/login', methods=('GET', 'POST'))
# def login():
#     if request.method == 'POST':
