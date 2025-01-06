#!/usr/bin/python
'''Loop through random lines from input file given as sys.argv[1] ('-' for stdin)
Lines consist of two fields delimited by '\t'
First part is Tagalog, second part is English or vice versa
Will print the first part, wait for input, then print the translation
if sys.argv[2] is 'r', will print English first.
'''
import random
import sys
import time
import argparse
import re

parser = argparse.ArgumentParser(description='Flashcard generator.')

parser.add_argument('-r', dest='reverse', action='store_true',
                    help='present second column rather than first, ie eng-tag')
parser.add_argument('-n', dest='norandom', action='store_true',
                    help="don't do random order, just go straight through")
parser.add_argument('-a', dest='autosleep', help="proceed to next after sleep, no keyboard input needed")
parser.add_argument('-c', dest='count', help='cards to do, 0 for "all"')
parser.add_argument('-s', dest='startline', help='start on this line.  default is 1.')
parser.add_argument('infile', help='input file')

args = parser.parse_args()

_mysep='\t'

f = open(args.infile, 'r') 

# read input:
myinput = f.read()

startline = 1
if args.startline:
    startline = int(args.startline)

if args.count:
    dothismany = 99999 if int(args.count) == 0 else int(args.count)
else:
    dothismany = 10

inc = 0
# split input into a list of lines:
alllines = myinput.split('\n')
mylist = alllines[startline-1:]
#mylist.pop()
#print(mylist)

count=linecount=0
_didalready = []
availablelines = len(mylist)
while count < dothismany and linecount <= availablelines:
    if not args.norandom:
        random.shuffle(mylist)

    try:
        myout = mylist.pop(0)
        linecount = linecount + 1
    except:
        print('ubós na..')
        exit()
    
    if myout.find(_mysep) < 0:
        continue

    t2e = myout.split(sep=_mysep, maxsplit=1)
    if len(t2e) < 2:
        continue

    count = count + 1
    print(count, '', end='')

    if args.reverse:
        _clue = t2e[1].strip()
        _match = re.match(r'(.*]) (.*)', _clue)
        if _match:
            _clue = _match[2]
        if args.autosleep:
            print(_clue)
            time.sleep(int(args.autosleep))
            print('\t', t2e[0].strip())
            time.sleep(int(args.autosleep))
        else:
            #print(t2e[1].strip(), end='')
            print(_clue, end='')
            input() # this will not work if reading input text from stdin!!!
            print('\t', t2e[0].strip())
        time.sleep(2) 
        print()
    else:
        if args.autosleep:
            print(t2e[0].strip())
            time.sleep(int(args.autosleep))
            print('\t', t2e[1].strip())
            time.sleep(int(args.autosleep))
        else:
            print(t2e[0].strip(), end='')
            input() # this will not work if reading input text from stdin!!!
            print('\t', t2e[1].strip())
        time.sleep(2) 
        print()
    
