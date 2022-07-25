#!/usr/bin/env python3
# given args which are a number of patterns to match against the foo_ affix
# strings in roots.txt, return all the roots and their corresponding matches for
# roots that match each pattern

import sys
import re

patternz = sys.argv[1:]

linez = []
with open('roots.txt') as f:
    for line in f:
         linez.append(line)

rootz = set()
for line in linez:
    m = re.match(r'.*?\(([^ ]*)\)', line)
    try:
        rootz.add(m.group(1))
    except Exception as e:
        print('got this', e, 'for', line)

for root in rootz:
    for p in patternz:
        if 
    print(root)
