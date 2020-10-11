#!/usr/bin/env python3
import sys
import re
from collections import defaultdict

_a = '[aAáàâ]'
_e = '[eEé]'
_i = '[iIíìî]'
_o = '[oOóòô]'
_u = '[uUú]'

with open('roots.txt', 'r') as f:
    dats = f.read()

for line in dats.split('\n'):
    if not re.match(r'^\S+ \(', line):
        continue
    word_, root_, _ = line.split(' ', maxsplit=2)
    word_ =  word_.strip() # toss any leading, trailing spaces
    root_ =  root_[1:-1] # toss open, close parens

    newsearch = ''
    for l in root_:
        if l == 'a':
            newsearch = newsearch + _a
        elif l == 'e':
            newsearch = newsearch + _e
        elif l == 'i':
            newsearch = newsearch + _i
        elif l == 'o':
            newsearch = newsearch + _o
        elif l == 'u':
            newsearch = newsearch + _u
        else:
            newsearch = newsearch + l
    
    #print(newsearch)
    tmatch = re.compile(f'^{newsearch}$', flags=re.IGNORECASE)
    if tmatch.search(word_):
        print(line)
