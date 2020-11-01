var page = require('webpage').create(),
system = require('system'), address;

// address = 'https://www.tagalog.com/words/sa.php';
address = system.args[1];
page.open(address, function () {
var count = 0

  // Check for the bottom div and scroll down from time to time
  window.setInterval(function() {
      // Check if there is a div with class=".has-more-items" 
      // (not sure if there's a better way of doing this)
      // var count = page.content.match(/class=".has-more-items"/g);

      // if(count === null) { // Didn't find
      if(count < 3) { // Didn't find
        count = count + 1
        page.evaluate(function() {
          // Scroll to the bottom of page
          window.document.body.scrollTop = document.body.scrollHeight;
        });
      }
      else { // Found
        // Do what you want
        console.log(page.plainText);
        phantom.exit();
      }
  }, 500); // Number of milliseconds to wait between scrolls

});