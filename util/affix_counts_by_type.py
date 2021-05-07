#!/usr/bin/env python3
import re
from collections import defaultdict

_file =  'roots.txt'

noun_affix_count = defaultdict(int)

for l in open(_file, 'r'):
  mo=re.search(r'(\S*_\S*) \[noun\]', l)
  #mo=re.search(r'(\w*_\w*) \[(\w+)\]', l)
  if mo and mo.lastindex == 1:
    affix = mo[1]
    noun_affix_count[affix] += 1

for prefix, count in noun_affix_count.items():
  print(count, prefix)
