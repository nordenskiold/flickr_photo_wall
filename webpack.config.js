const path = require('path');
const webpack = require('webpack');
const ExtractTextPlugin = require('extract-text-webpack-plugin');

module.exports = {
	context: path.resolve(__dirname, './node_modules'),
	entry: {
	    app: [
			'./jquery/dist/jquery.min.js',
			'./popper.js/dist/umd/popper.js',
			'./snackbarjs/dist/snackbar.min.js',
			'./socket.io-client/dist/socket.io.slim.js',
			'./jquery-bridget/jquery-bridget.js',
			'./masonry-layout/dist/masonry.pkgd.min.js',
			'./bootstrap-material-design/dist/js/bootstrap-material-design.min.js',
			'./bootstrap-material-design/dist/css/bootstrap-material-design.css',
			'../flickr_photo_wall/static/src/js/entry.js',
			'./roboto-fontface/css/roboto/roboto-fontface.css',
			'./@icon/open-iconic/open-iconic.css',
			'../flickr_photo_wall/static/src/css/entry.css'
        ]
    },
	output: {
		path: path.resolve(__dirname, './flickr_photo_wall/static'),
		filename: 'dist/[name].js'
	},
	module: {
		loaders: [
			{
				test: /\.css$/,
				loader: ExtractTextPlugin.extract("css-loader")
			},
			{
				test: /\.woff(2)?(\?v=[0-9]\.[0-9]\.[0-9])?$/,
				loader: "url-loader?publicPath=../&name=./../static/fonts/[hash].[ext]&limit=10000&mimetype=application/font-woff"
			},
			{
				test: /\.(ttf|eot|svg)(\?v=[0-9]\.[0-9]\.[0-9])?$/,
				loader: "file-loader?publicPath=../&name=./../static/fonts/[hash].[ext]"
			},
			{ test: /\.png$/, loader: "url-loader?mimetype=image/png" },
			{ test: /\.gif$/, loader: "url-loader?mimetype=image/gif" }
		]
	},
		plugins: [
			new ExtractTextPlugin("../static/dist/[name].css"),
			new webpack.ProvidePlugin({
      			$: "jquery",
      			jQuery: "jquery",
				Popper: 'popper.js/dist/umd/popper.js'
    		})
		]
};