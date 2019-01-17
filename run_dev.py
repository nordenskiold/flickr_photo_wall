"""This file is used for running the app locally"""

from flickr_photo_wall import setup_app

app, socketio = setup_app(config='default')
socketio.run(app=app, port=8080, host='0.0.0.0', debug=True)
