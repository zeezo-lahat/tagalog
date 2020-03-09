#!/bin/bash
# for each root, list horizontally the verb affixes
for r in $(grep -F '[verb' roots.txt | sed 's/).*//' | sed 's/.* (//' | uniq); do
   a=$(grep "($r) .*\[verb" roots.txt | grep '_.* \[verb' | sed "s/.*) //" | sed 's/ .*//')
   echo $r $a
done 
