"""flickr_photo_wall search view"""

import flask
from flask import render_template
from flask_socketio import emit

from flickr_photo_wall import socketio
from flickr_photo_wall.controllers.flickr_api import FlickrAPI

search_view = flask.Blueprint(
    'search',
    __name__,
    template_folder='templates',
    static_folder='static')


@search_view.route('/')
def index():
    """The default route for this app"""
    return render_template('index.html')


@socketio.on('search')
def search_listener(request):
    """A socketio listener for incoming search requests"""
    tags = filter(None, request['search'].split(' '))
    flickr = FlickrAPI()
    result = flickr.get_images_by_tags(tags)
    emit('search', result, json=True)
