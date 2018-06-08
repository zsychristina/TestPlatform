
// Simple Javascript example

var page = require('webpage').create();

var url = 'http://www.testfan.cn/list/2/220.htm';
page.open(url, function (status) {
  //Page is loaded!
    var start = performance.timing.responseStart;
    var stop = performance.timing.domComplete;
    console.log(stop - start);
    page.render('python.png');
    phantom.exit();
});
