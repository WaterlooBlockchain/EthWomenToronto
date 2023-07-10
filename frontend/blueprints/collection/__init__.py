from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

collection = Blueprint('collection', __name__)

@collection.route('/')
def show(page):
    try:
        return render_template(f'collection/{page}.html')
    except TemplateNotFound:
        abort(404)

