#!/usr/bin/env python3
'''add defs to words.txt from stdin

stdin will be a word/phrase definition.  a tab or newline will separate the word from the def.
procedure:
    - read stdin
    - format stdin:
        will become single line as <word/phrase>\t<def>
        very forgiving:
            if no tab or newline, first space will become separator, otherwise first newline/tab will become separator
                any subsequent tabs/newlines will be mapped into spaces as needed
    - read words.txt into list.
    - append new entry to the list
    - sort and print the list
    - have a nice day
'''

# aside, read this string into datetime obj? : 4/29/2017 12:00:00 AM

import sys
import re
myfile = 'words.txt'
with open(myfile, 'r') as f:
    _old =  f.read()
lines=_old.split('\n')
lines.pop() # toss the empty final element
_new = sys.stdin.read()
def format_input(dat):
    if not re.search(r'\S\s+\S', dat): # require word and def, separated by whitespace
        return False
    dat = re.sub(r'^\s+', '', dat) # toss any leading whitespace
    dat = re.sub(r'\s+$', '', dat) # toss any trailing whitespace
    dat = re.sub(r'\n', '\t', dat, count=1) # map the first newline to a tab
    dat = re.sub(r'\s*\t\s*', '\x00', dat, count=1) # map the first tab plus any surrounding whitespace to a null byte
    dat = re.sub(r'[\t\n]+', ' ', dat) # map any subsequent newlines or tabs to spaces
    if not re.search(r'\x00', dat): # if there's no null byte, the first space(s) becomes a null byte
        dat = re.sub(r'\s+', '\x00', dat, count=1)
    dat = re.sub('  *', ' ', dat) # consecutive spaces become single spaces
    dat = re.sub(r'\x00', '\t', dat) # null byte becomes tab
    return dat

_new_def = format_input(_new)
lines.append(_new_def)
#lines.sort(key=str.lower)
lines.sort()
for l in lines:
    print(l)
