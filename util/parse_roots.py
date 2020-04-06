#!/usr/bin/env python3
import sys
import re
f = open(sys.argv[1], 'r')
d = f.read()
root = re.sub(r'.*Example words using the Filipino / Tagalog root "(.*?)".*', r'\1', d, flags=re.DOTALL)
meat = re.sub(r'.*Example words using the Filipino / Tagalog root ".*?".*?\n *(.*?)Join us.*', r'\1', d, flags=re.DOTALL)
entries = re.split(r' *\[\d+\]more\..*?\xbb', meat, flags=re.DOTALL)  # want to split on " *[999]more" up through "\xbb"
for i in entries:
    i = re.sub(r'^\W*\[.*?\]', '', i)  # remove leading [999]
    i = re.sub(r'\n', '', i)  # remove newline
    i = re.sub(r'  *', ' ', i)  # remove multiple spaces
    i = re.sub(r':', '(' + root + ')', i)  # surround with parens
    if len(i) > 1:
        print(i)

'''
[31]karaniwan : [adjective] common; usual; widespread; habitual;
   average; colloquial [adverb] commonly; generally; in general; chiefly;
   customarily   [32]more... »
   [33]di-pangkaraniwan : [adjective] unusual; peculiar; extraordinary
   [34]more... »
   [35]pinakakaraniwan : [adjective] commonest; most common   [36]more...
   »
'''
