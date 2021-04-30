#!/usr/bin/env python3
import re
from collections import defaultdict

_file =  'roots.txt'

noun_affix_count = defaultdict(int)

for l in open(_file, 'r'):
  mo=re.search(r'(\w*_\w*) \[noun\]', l)
  #mo=re.search(r'(\w*_\w*) \[(\w+)\]', l)
  if mo and mo.lastindex == 1:
    affix = mo[1]
    noun_affix_count[affix] += 1

for k, v in noun_affix_count.items():
  print(k, v)

f = open('roots.txt', 'r')

d = f.read()
all = re.split(r'( _ | _\w+|\w+_ | _\w+_ | [a-zCV]+_[a-z]+ )', d)

c = defaultdict(int)
for l in all:
    try:
        l.index('_')
        c[l] += 1
    except:
        continue

for k, v in c.items():
    print(v, '\t', k.strip())
