#!/usr/bin/python3.7
'''Input .td files, output the english phrase -> tagalog translations,
so that, eg., this:

abiso •

   n.
     *
          + notice, notification mag-abiso, iabiso, abisuhan (mag-:i-:-an)

   v.
     *
          + to announce, to inform, to notify. Abisuhan mo si Juan ng
            aking pagdating. Notify John about my arrival.

» synonyms and related words:

   advice
   v.
     *
          + 1. an opinion about what should be done: payo, pangaral,
            tagubilin
          + 2. news, information: balita, pabalita


Becomes:

an opinion about what should be done: payo, pangaral, tagubilin
news, information: balita, pabalita

We want to split input on '^ {9,}\+ +\d+\. *'
'''

import sys
import re

myin = sys.stdin.read()

# MULTILINE makes "^"/"$" match at the beginning/end of each line
mysplitpattern = re.compile(r'^ {9,}\+ *\d*\.* *', flags=re.MULTILINE)
#mysplitpattern = re.compile(r'^ {9,}\+ +\d+\. *', flags=re.MULTILINE)

# toss stuff we don't want at the end of our strings:
mytrailingcruftpattern = re.compile('\n\n.*', flags=re.DOTALL) 

myentries = re.split(mysplitpattern, myin)
myentries.pop(0) # toss the stuff that precedes our first splitpattern match

multispacepattern = re.compile(r'\s+')

for e in myentries:
    t2e = []
    e = re.sub(mytrailingcruftpattern, '', e)
    e = re.sub(multispacepattern, ' ', e) # replace all \s+ with ' '
    t2e[:] = e.split(': ')
    try:
        print(t2e[1].strip() + '\t' + t2e[0].strip())
    except:
        continue
    #e = re.sub(r':', '\t', e)
    #print("{0}".format(e))

exit(0)
