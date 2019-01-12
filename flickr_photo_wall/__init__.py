from flask import Flask


def create_app(config="Default"):
    """Create a new flask application"""
    app = Flask(__name__, instance_relative_config=True)
    configure_cfg(app, config)
    configure_bp(app)
    return app

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
    app.register_blueprint(search.search_view, url_prefix='/search')


if __name__ == '__main__':
    app = create_app()
    app.run()
