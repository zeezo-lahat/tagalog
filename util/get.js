var page = require('webpage').create(),
  system = require('system'), address;

address = system.args[1];
page.scrollPosition= { top: 1000, left: 0}  
page.open(address, function(status) {
  if (status !== 'success') {
    console.log('** Error loading url.');
  } else {
    page.scrollPosition= { top: page.scrollPosition + 1000, left: 0}
    console.log(page.plainText);
  }
  phantom.exit();
});
