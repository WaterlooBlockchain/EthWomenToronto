from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

auth = Blueprint('auth', __name__)

@auth.route('/')
def show(page):
    try:
        return render_template(f'auth/{page}.html')
    except TemplateNotFound:
        abort(404)
