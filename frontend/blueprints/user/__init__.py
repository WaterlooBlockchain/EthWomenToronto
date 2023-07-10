from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

user = Blueprint('user', __name__)

@user.route('/')
def show(user):
    try:
        return render_template(f'users/{user}.html')
    except TemplateNotFound:
        abort(404)
