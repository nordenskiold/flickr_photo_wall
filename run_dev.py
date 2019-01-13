from flickr_photo_wall import create_app

app = create_app(config='default')
app.run(port=8080, host='0.0.0.0', threaded=True, debug=True)
