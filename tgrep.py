from collections import defaultdict
import sys
import re

_a = '[aAáàâ]'
_e = '[eEé]'
_i = '[iIíìî]'
_o = '[oOóòô]'
_u = '[uUú]'

_d = defaultdict(int)

_mychars = set()

try:
    myfile = open(sys.argv[1], 'r')
    mysearchstring = sys.argv[2]
except:
    print('I need a filename and a pattern to search, dumb-ass')
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

tmatch = re.compile(newsearch)

while 1:
  c = myfile.readline()
  if c:
      c = c.strip()
      if tmatch.search(c):
          print(c)
  else:
      break
  