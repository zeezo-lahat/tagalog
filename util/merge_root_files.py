#!/usr/bin/env python3
# merge 2 roots files given on command line.  writes to stdout
import sys
import re
f = open(sys.argv[1], 'r')
g = open(sys.argv[2], 'r')
d = f.read()
e = g.read()
_dat = d + e # string containing contents of files

# get list of roots:
roots =  set()
for _line in re.split(r'\r*\n', _dat):
    _m = re.search(r'\(.+?\)', _line)
    if _m:
        if not _m.group() in roots:
             roots.add(_m.group())
    
print('got', len(roots), 'roots')

for _r in sorted(roots):
    _r = re.sub(r'\(', '\(', _r) # escape leading '('
    _r = re.sub(r'\)', '\)', _r) # escape ending ')'
    _p = r'.*' + _r + '.*'
    _strpat = re.compile(_p, flags=re.MULTILINE)
    _r_conjugations = re.findall(_strpat, _dat)
    if isinstance(_r_conjugations, list):
        for _conj in sorted(_r_conjugations):
            print(_conj)

exit()
