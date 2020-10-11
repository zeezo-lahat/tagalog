#!/bin/bash -x

# get current list of roots from roots.txt and put in root_list.txt
# pull down the current list of roots from tagaloglessons.com roots page, store in roots_latest.txt
# find the ones that are not in root_list.txt and write to need.txt
# for files in need.txt, pull down their pages and put them each in tmp/roots/
# for each file in tmp/roots/, run parse_roots.py on it and append to more_roots.txt

if [ -e roots.txt ] && [ -e tmp ]; then
  :
else
  echo "wrong dir, dummy"
  exit 1
fi

rm -rf tmp/roots/ 2>/dev/null
mkdir tmp/roots/ || exit 1

sed "s/[^(]* (//" roots.txt | sed "s/).*//"| sort | uniq > root_list.txt
lynx -dump https://www.tagaloglessons.com/dictionary/roots.php > roots_latest.txt
sed -i '1,/common roots below/d; /Root count/,$d; s/\[[0-9]*\]//g; s/^ *//' roots_latest.txt
for f in $(<roots_latest.txt); do grep -q "^$f$" root_list.txt || echo $f; done > need.txt
for f in $(<need.txt); do echo $f; lynx -dump "https://www.tagaloglessons.com/dictionary/root.php?root=$f&back=Roots" >tmp/roots/$f.txt; done
for f in tmp/roots/*.txt; do ./util/parse_roots.py $f; done >more_roots.txt
./util/merge_root_files.py roots.txt more_roots.txt | uniq >_r00ts
mv _r00ts roots.txt
rm need.txt more_roots.txt 2>/dev/null
