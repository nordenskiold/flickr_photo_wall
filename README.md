# Flickr Photo Wall

### About
This project contains a web app that displays photos from flickr's public API. Users can search photos by tags and are presented with a slideshow of the results. The API is polled in intervals and the results will update dynamically as new images are uploaded to flickr. The slideshow will always display the latest photos returned from the API and cull older results.

You can demo this project [here] 

*TODO*: Insert link

### Requirements
This project uses [Virtualenv](https://virtualenv.pypa.io/en/latest/) to manage its python dependencies.

* Python 3.7.x
* Pip 18.1
* Virtualenv

### Setup
```
$ cd flickr_photo_wall
$ pip install virtualenv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ fab command to install js dependencies
$ python run_dev.py
```

### Testing
`fab task goes here`



