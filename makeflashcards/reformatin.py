#!/usr/bin/python3.7

import re

i = 0

with open('out1.txt', 'r') as infile:
    for line in infile:
        if re.search('$^', line): # blank line
            i = 0
            continue
        if i == 0:
            tag = line.strip()
            i = 1
            continue
        eng = line.strip()
        print(tag, '	', eng)
