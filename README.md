# Flickr Photo Wall

### About
This project contains a web app that displays photos from flickr's public API. Users can search photos by tags and are presented with a slideshow of the results. The API is polled in intervals and the results will update dynamically as new images are uploaded to flickr. The slideshow will always display the latest photos returned from the API and cull older results.


### Requirements
This project uses [Virtualenv](https://virtualenv.pypa.io/en/latest/) to manage its python dependencies, and [Node Package Manager](https://www.npmjs.com/) to manage its javascript dependencies. The following is a list of packages required to run this project and the versions this project has been tested with.

* Python 3.7.2
* Pip 18.1
* Virtualenv 15.0.1
* NPM 5.6.0 

### Setup
```
$ cd flickr_photo_wall
$ pip install virtualenv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ npm run bundle-dev
$ python run_dev.py
```

### Testing
`TBD`



