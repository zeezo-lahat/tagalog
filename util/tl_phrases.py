#!/usr/bin/python
'''Input .tl files, output tagalog phrase -> english translations
reads from stdin, writes to stdout

also catch:
    lines with ":.+" surrounded by blank lines are <word/phrase> : <def>

    lines with ":.+" preceded by blank line and followed by non-blank line(s) are <word/phrase> : <def 1> <def 2>

    lines beginning with '^ *=' are continuation lines

    if there are 4 consecutive lines, it is 
    if there are 3 consecutive lines, it is <phrase/word> <def part 1> <def part 2>

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
