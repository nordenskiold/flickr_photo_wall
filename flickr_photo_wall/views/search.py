"""flickr_photo_wall search view"""

import flask
from flask import current_app, render_template

search_view = flask.Blueprint(
    'search',
    __name__,
    template_folder='templates',
    static_folder='static')


@search_view.route('/')
def index():
    return render_template('index.html')