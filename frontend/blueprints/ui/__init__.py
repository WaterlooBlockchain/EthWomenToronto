from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

ui = Blueprint('ui', __name__)

@ui.route('/')
def show(component):
    try:
        return render_template(f'ui/{component}.html')
    except TemplateNotFound:
        abort(404)
