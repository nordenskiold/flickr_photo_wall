from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__, instance_relative_config=True)
socketio = SocketIO(app)


def setup_app(config="Default"):
    """Configure the flask app and return references"""
    configure_cfg(app, config)
    configure_bp(app)
    return app, socketio


def configure_cfg(app, config):
    """Configure flask config files

    Additional conditional config files will be added here as the project grows
    """
    app.config.from_object('config.' + config)


def configure_bp(app):
    """Configure application blueprints

    Additional blueprints will be added here as the project grows
    """
    from flickr_photo_wall.views import search
    app.register_blueprint(search.search_view, url_prefix='/')


if __name__ == '__main__':
    app, socketio = setup_app()
    socketio.run(app=app, port=8080, host='0.0.0.0', debug=True)
