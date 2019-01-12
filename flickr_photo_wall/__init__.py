from flask import Flask


def create_app(config=None):
    """Create a new flask application"""
    app = Flask(__name__, instance_relative_config=True)
    configure_bp(app)
    return app


def configure_bp(app):
    """Configure application blueprints"""
    from flickr_photo_wall.views import search

    app.register_blueprint(search.search_view, url_prefix='/search')


if __name__ == '__main__':
    app = create_app()
    app.run()
