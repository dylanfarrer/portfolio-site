from flask import Blueprint, render_template

bp = Blueprint('main', __name__)

@bp.route('/')
def my_home():
    return render_template('about.html')

@bp.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)