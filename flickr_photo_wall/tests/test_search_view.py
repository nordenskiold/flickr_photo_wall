from flickr_photo_wall.tests.base import FlickrPhotoWallTestCase


class SearchViewTestCase(FlickrPhotoWallTestCase):
    """Test cases for the search view"""

    def test_get(self):
        """It renders the search view"""
        ret = self.client.get('/')
        assert ret.status_code == 200
        assert 'flickr Image Search' in ret.data
