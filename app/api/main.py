from flask import render_template
from app.api import bp_main


@bp_main.route('/')
def home():
    return bp_main.send_static_file('index.html')


@bp_main.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
