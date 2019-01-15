"""flickr_photo_wall search view"""

import flask
from flask import render_template
from flask_socketio import emit

from flickr_photo_wall import socketio
from flickr_photo_wall.controllers.search import FlickrAPI

search_view = flask.Blueprint(
    'search',
    __name__,
    template_folder='templates',
    static_folder='static')


@search_view.route('/')
def index():
    return render_template('index.html')


@socketio.on('search')
def search_listener(request):
    tags = filter(None, request['search'].split(' '))
    flickr = FlickrAPI()
    result = flickr.search_by_tags(tags)
    print('\n\n\nreceived tags: ' + str(tags) + '\n\n\n')
    emit('search', result, json=True)
