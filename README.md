# Flickr Photo Wall

### About
This project contains a web app that displays photos from flickr's public API. Users can search photos by tags and are presented with a slideshow of the results. The API is polled in intervals and the results will update dynamically as new images are uploaded to flickr. The slideshow will always display the latest photos returned from the API and cull older results. Live demo coming soon.

![](flickr_photo_wall_demo.gif)

### Requirements
This project uses [Virtualenv](https://virtualenv.pypa.io/en/latest/) to manage its python dependencies, and [Node Package Manager](https://www.npmjs.com/) to manage its javascript dependencies. The following is a list of packages required to run this project and the versions this project has been tested with.

* Python 2.7.12
* Pip 18.1
* Virtualenv 15.0.1
* NPM 5.6.0 

Tested working on Firefox 63.0, Chrome 71 on Ubuntu and Windows 10.

### Setup

Clone repo and navigate to repo directory

```
$ git clone https://github.com/nordenskiold/flickr_photo_wall.git
$ cd flickr_photo_wall
```

Install, initialize and activate virtualenv
```
$ pip install virtualenv==15.0.1
$ virtualenv env
$ source env/bin/activate
```

Install dependencies
```
$ (env) pip install -r requirements.txt
$ npm install
$ npm run bundle-dev
```

### Running the Project
```
$ cd flickr_photo_wall
$ python run_dev.py 
```
You should now have a web server running by default on [http://0.0.0.0:8080](http://0.0.0.0:8080)

### Testing
This project uses [pytest](https://github.com/pytest-dev/pytest) and [flask-testing](https://github.com/jarus/flask-testing) for testing. To run tests, simply:

`$ (env) python -m pytest -v flickr_photo_wall/tests/`

