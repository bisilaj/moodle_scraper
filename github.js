var page = require('webpage').create();
page.open('http://moodle.carleton.edu/', function() {
  page.render('github.png');
  phantom.exit();
});