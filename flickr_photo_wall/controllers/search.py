"""Flickr API Controller"""
import json
import os
import requests
from flask import current_app


class FlickrAPI(object):
    """"""

    def __init__(self):
        """"""
        self.search_url = os.path.join(current_app.config['FLICKR_API_URL'],
                                       current_app.config['FLICKR_PHOTOS_URL'])

    def search_by_tags(self, tags):
        """"""
        params = {'tags': tags, 'format': 'json', 'nojsoncallback': 1}
        res = requests.get(url=self.search_url, params=params)
        print('\n\n\n\n\n')
        print(res.content)
        print('\n\n\n\n\n')

        new_res = []
        print('\n\n\n\n\n\n')
        items = json.loads(res.content)['items']
        for image in items:
            new_res.append(image['media']['m'])

        return new_res