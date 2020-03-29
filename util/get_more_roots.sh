#!/bin/bash -x

# to do: add commands to need to run parse_roots.py, update root_list.txt, rm tmp/*

rm tmp/* 2>/dev/null
lynx -dump https://www.tagaloglessons.com/dictionary/roots.php > roots_latest.txt
sed -i.bar '1,/common roots below/d; /Root count/,$d; s/\[[0-9]*\]//g; s/^ *//' roots_latest.txt
for f in $(<roots_latest.txt); do grep -q "^$f$" root_list.txt || echo $f; done > need.txt
for f in $(<need.txt); do echo $f; lynx -dump "https://www.tagaloglessons.com/dictionary/root.php?root=$f&back=Roots" >tmp/$f.txt; done
rm need.txt

