from flask import Blueprint, render_template

blueprint = Blueprint('/', __name__)


@blueprint.route('/')
@blueprint.route('/home')
def home():
    return render_template('home.html')


@blueprint.route('/contact')
def contact():
    return render_template('contact.html')
