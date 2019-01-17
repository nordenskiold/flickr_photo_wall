"""This file is used for running the app on heroku"""

from flickr_photo_wall import setup_app

app, _ = setup_app(config='default')
