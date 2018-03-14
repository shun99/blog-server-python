from flask import render_template
from app.api import b_main


@b_main.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
