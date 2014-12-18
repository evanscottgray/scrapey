var page = require('webpage').create();
var url = phantom.args[0];
page.open(url);
page.onLoadFinished = function()
{
    window.setTimeout(function () {
        var html = page.evaluate(function () {
            return document.getElementsByTagName('html')[0].innerHTML;
        });
        console.log(html);
	phantom.exit();
    }, 2000);
};
