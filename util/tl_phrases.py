#!/usr/bin/python3.7
'''Input .tl files, output tagalog phrase -> english translations
reads from stdin, writes to stdout

example input:

LIWANAG

   ilaw, tanglaw, sindi, sinag; kalinawan, klaro
   liwanag, n
   light, shine

   maliwanag, adj
   bright, clear, explicit

   lumiwanag, v
   to clear up, to brighten

   ipaliwanag, v
   to explain, to make clear, to clarify

   [66]paliwanag, n
   explanation

   liwanag sa dilim
   brightness in the dark, light in the darkness

   nagbibigay-liwanag
   luminous

   Liwanag is also a native Tagalog surname of many Filipinos.

becomes:

liwanag sa dilim   brightness in the dark, light in the darkness

etc.

These files have a pattern of:

<blank line>
<tagalog line>
<english translation>
<blank or line of __*>

We will toss everything else, though this will mean we will miss some things.

We will use findall to pull all patterns of this form:
   '(^\s+[a-zA-Z].*\n){2}' (MULTILINE, non-DOTALL)

'''

import sys
import re

myin = sys.stdin.read()

# MULTILINE makes "^"/"$" match at the beginning/end of each line
# NOTE that using the non-capturing (?:...) group is needed here, otherwise
#   the {2} doesn't work properly with just (...) for some reason
mypattern = re.compile(r'^[_]*$\n(?:^ +.*[a-zA-Z].*\n){2}^[_]*$', flags=re.MULTILINE)

myentries = re.findall(mypattern, myin)


for e in myentries:
    e = e.strip()
    e = re.sub(r'\n *', '\t', e)
    print("{0}".format(e))

exit(0)
