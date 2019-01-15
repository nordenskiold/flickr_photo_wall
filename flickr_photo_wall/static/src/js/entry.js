var $ = require('jquery');
var jQueryBridget = require('jquery-bridget');
var Masonry = require('masonry-layout');
jQueryBridget( 'masonry', Masonry, $ );

window.Popper = require('popper.js')
window.io = require('socket.io-client');
window.jQuery = $;
window.$ = $;

