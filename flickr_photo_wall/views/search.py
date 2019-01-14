"""flickr_photo_wall search view"""

import flask
from flask import current_app, render_template

from flickr_photo_wall import socketio

search_view = flask.Blueprint(
    'search',
    __name__,
    template_folder='templates',
    static_folder='static')


@search_view.route('/')
def index():
    return render_template('index.html')


@search_view.route('/result', methods=['POST', 'GET'])
def result():
    return render_template('index.html')


@socketio.on('my event')
def handle_my_custom_event(json):
    print('received json: ' + str(json))