#!/usr/bin/python3.7
'''Input text in sentences.  Output count of n-word phrases, n >= 1
   Input is given by sys.argv(1) - either an input filename or '-' for stdin.
'''
import sys
import re
import collections

myout = open("words.txt", "w")

if len(sys.argv) == 1:
    print("Hey!  I need an input filename or '-'")
    exit(1)

# What is my input?
if sys.argv[1] is "-":
    f =  sys.stdin
else:
    f = open(sys.argv[1], 'r') 

# read input:
myinput = f.read()

# initialize all my many, many params:
d = {}
wordsinsentence = []
numwordsinsentence = 0
mykey = ""
endofsentence = False

for myword in myinput.split():
    numwordsinsentence += 1
    if myword.endswith('.') or myword.endswith('?') or myword.endswith('!'):
        endofsentence = True
        myword = myword.replace('.','')
        myword = myword.replace('?','')
        myword = myword.replace('!','')
    d[myword] = d.get(myword, 0) + 1
    wordsinsentence.append(myword)
    # here I need to create/increment keys for 1 - 
        mykey = mykey + " " + myword
    print("my phrase is: {}".format(mykey))
    if endofsentence is True:
        # reset lahat!!!!
        numwordsinsentence = 0
        wordsinsentence = []
        mykey = ""
        endofsentence = False

'''
for k, v in d.items():
    print(v, ' ', k)
'''
