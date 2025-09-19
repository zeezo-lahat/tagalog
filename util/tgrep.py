#!/usr/bin/env python
"""grep for"""
import re
import sys
from collections import defaultdict

# expand matches for the vowels, so that eg "a" matches "à", "á", etc.
_a = '[aáàâAÁÀÂ]'
_e = '[eéEÉ]'
_i = '[iíìîIÍÌÎ]'
_o = '[oóòôOÓÒÔ]'
_u = '[uúUÚ]'

_d = defaultdict(int)

_mychars = set()

try:
    #myfile = open(sys.argv[1], 'r')
    myfile = sys.stdin
    #mysearchstring = sys.argv[2]
    mysearchstring = sys.argv[1]
except:
    print('I need a filename and a pattern to search..')
    exit(1)

newsearch = ''
for l in mysearchstring:
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

#newsearch = newsearch + '.*\t'
tmatch = re.compile(newsearch, flags=re.IGNORECASE)

while 1:
  c = myfile.readline()
  if c:
      c = c.strip()
      if tmatch.search(c):
          print(c)
  else:
      break
  
