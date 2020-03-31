#!/usr/bin/env python3
'''
remove carriage returns from file given as argv[1]
print to stdout
'''
import sys
f = open(sys.argv[1], 'r')

while 1:
  c = f.read(1)
  if c:
    if c != '\r':
      print(c, end='')
  else:
    break
