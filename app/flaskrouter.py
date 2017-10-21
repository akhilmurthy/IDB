from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

flaskrouter = Blueprint('flaskrouter', __name__)

@flaskrouter.route('/')
def frindex():
    try:
        return render_template('index.html')
    except TemplateNotFound:
        abort(404)

@flaskrouter.route('/about')
def frabout():
    try:
        return render_template('about.html')
    except TemplateNotFound:
        abort(404)

"""
@flaskrouter.route('/')
@flaskrouter.route('/<page>')
def show(page):
    try:
        return render_template('pages/%s.html' % page)
    except TemplateNotFound:
        abort(404)
"""