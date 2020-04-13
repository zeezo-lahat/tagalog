#!/bin/bash
# reads from stdin, writes to stdout
# input is text with alternating lines of tagalog and english translations
IFS=$'\n'
z=0
for n in $(cat); do
   z=$((z+1))
   if [ $((z%2)) == 1 ]; then
      echo -en "$n\t"
   else
      echo $n
   fi
done
