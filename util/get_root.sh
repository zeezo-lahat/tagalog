#!/bin/bash

if [ ${#1} -gt 0 ]; then
  f=$1
  #echo $f
else
  echo I need a param
  exit 1
fi

#lynx -dump "https://www.tagaloglessons.com/dictionary/root.php?root=$f&back=Roots" >.out
lynx -dump "https://www.tagalog.com/dictionary/root-word-$f" >.out
./util/parse_roots.py .out
rm .out
