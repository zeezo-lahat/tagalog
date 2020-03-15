#!/usr/bin/env python3
import re
from collections import defaultdict

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
