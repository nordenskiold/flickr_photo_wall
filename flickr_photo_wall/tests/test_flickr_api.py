from mock import patch

from flickr_photo_wall.controllers.flickr_api import FlickrAPI
from flickr_photo_wall.tests.base import FlickrPhotoWallTestCase


class SearchTestCase(FlickrPhotoWallTestCase):
    """Test cases for FlickrAPI controller"""

    @patch('flickr_photo_wall.controllers.flickr_api.requests')
    def test_get_images_by_tags(self, requests_mock):
        """Test get_images_by_tags function"""

        mock_response = """
        {
		    "items": [
               {
                    "title": "Photo",
                    "media": {"m":"https:\/\/farm5.staticflickr.com\/4918\/31820194797_6cdf1587bc_m.jpg"}
               },
               {
                    "title": "Photo2",
                    "media": {"m":"https:\/\/farm5.staticflickr.com\/4918\/57422146782_1dpq9914zw_m.jpg"}
               }
	        ]
        }
        """

        requests_mock.get.return_value.content = mock_response
        api = FlickrAPI()
        tags = ['funny', 'cat']
        res = api.get_images_by_tags(tags=tags)
        assert type(res) == list
        assert len(res) == 2
        assert "https://farm5.staticflickr.com/4918/31820194797_6cdf1587bc_m.jpg" in res
        assert "https://farm5.staticflickr.com/4918/57422146782_1dpq9914zw_m.jpg" in res
