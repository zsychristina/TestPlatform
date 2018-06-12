console.log('Loading a web page');
var page = require('webpage').create();
var url = 'http://www.testfan.com/';
page.open(url, function (status) {
  //Page is loaded!
  page.render('python.jpg');
  phantom.exit();
});