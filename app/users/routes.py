from .models import User
from flask import Blueprint, render_template, request, url_for

blueprint = Blueprint('users', __name__)


@blueprint.route('/register', methods=('GET', 'POST'))
def register():
    # if request.method == 'POST':

    return render_template('users/register.html')
