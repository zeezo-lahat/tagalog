#!/bin/bash

if [ ${#1} -gt 0 ]; then
  f=$1
  echo $f
else
  echo I need a param
  exit 1
fi

#lynx -dump "https://www.tagalog.com/words/$f.php"
#phantomjs util/get.js "https://www.tagalog.com/words/$f.php" | parse_defs.py > $f.txt
phantomjs util/scrolly.js "https://www.tagalog.com/words/$f.php" | parse_defs.py > $f.txt
