#!/usr/bin/python3.7
'''Fold lines from stdin so that they are no longer than sys.argv[1] chars

BUG: does not fold on tabs properly

For each line that is longer than maxlen chars, replace ' ' or \t with '\n' so that
the line length does not exceed maxlen.  

Don't try to form proper paragraphs, as the input text is not necessarily in paragraph
form. 

We will use this:
 |  rpartition(...)
 |      S.rpartition(sep) -> (head, sep, tail)
 |
 |      Search for the separator sep in S, starting at the end of S, and return
 |      the part before it, the separator itself, and the part after it.  If the
 |      separator is not found, return two empty strings and S.
 |

For the future:

  How to implement using recursion?

  Paragraph mode - all lines continue up to maximum length, except perhaps where
  there are blank lines.

'''

import sys

if len(sys.argv) != 2:
    print("Bro, I need a max line length")
    exit(1)

maxlen = int(sys.argv[1])

# read input:
myinput = sys.stdin.read()

# split input into a list of lines:
mylist = myinput.split('\n')

nc = ''
mylen = 0

# operate on each line
for line in mylist:
    for i, c in enumerate(line):
        mylen += 1
        if c in [' ', '\t']:
            spaceindex = i
        nc = ''.join([nc, c])
        if mylen > maxlen:
            (newc, _, nc) = nc.rpartition(' ')
            print(newc)
            mylen = len(nc)
            continue
    print(nc)
    nc = ''
    mylen = 0
