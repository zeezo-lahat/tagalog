'''
a A á à â
e E é
i I í ì î
o O ó ò ô
u U ú
'''
from collections import defaultdict
import sys
_d = defaultdict(int)
_mychars = set()
f = open(sys.argv[1], 'r')

while 1:
  c = f.read(1)
  if c:
      _mychars.add(c)
      _d[c] += 1
  else:
      break
  

for i, j in _d.items():
    #print(j, i)
    print(i, end='')
