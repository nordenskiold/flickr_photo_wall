"""Flickr API Controller"""
import json
import os
import requests
from flask import current_app


class FlickrAPI(object):
    """The FlickrAPI Class"""

    def __init__(self):
        """FlickrAPI constructor"""
        self.search_url = os.path.join(current_app.config['FLICKR_API_URL'],
                                       current_app.config['FLICKR_PHOTOS_URL'])

    def get_images_by_tags(self, tags):
        """Return a list of image urls given some tags"""
        params = {'tags': tags, 'format': 'json', 'nojsoncallback': 1}
        res = requests.get(url=self.search_url, params=params)

        items = json.loads(res.content)['items']
        image_url_list = [item['media']['m'] for item in items]

        return image_url_list
