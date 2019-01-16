from flask_testing import TestCase
import flickr_photo_wall


class FlickrPhotoWallTestCase(TestCase):
    """Base class for flickr_photo_wall testcases"""

    def create_app(self):
        """Create the flask application"""
        return flickr_photo_wall.setup_app()[0]

    def setUp(self):
        """Additional generic setup tasks go here"""
        pass
