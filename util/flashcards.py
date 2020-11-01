#!/usr/bin/python3.7
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

parser = argparse.ArgumentParser(description='Make flashcards from listen input files.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                            help='an integer for the accumulator')

if sys.argv[1] is "-":
    f =  sys.stdin
else:
    f = open(sys.argv[1], 'r') 

# read input:
myinput = f.read()

try:
    order = sys.argv[2] # if == "r" do english -> tagalog
except:
    order = ""

inc = 0
# split input into a list of lines:
mylist = myinput.split('\n')
mylist.pop()
#print(mylist)

count=0
_didalready = []
while count < 10:
    j = 0

    while True:
        j += 1
        myout = random.choice(mylist)
        if myout not in _didalready:
            _didalready.append(myout)
            break
        if j > 100:
            break

    if myout.find('	') < 0:
        continue

    t2e = myout.split(sep='	', maxsplit=1)
    if len(t2e) < 2:
        continue

    count = count + 1

    if order == "r":
        #print(t2e[1].strip())
        print(t2e[1].strip(), end='')
        input()
        #time.sleep(25) 
        print('\t\t\t\t', t2e[0].strip())
        time.sleep(2) 
        print()
    else:
        print(t2e[0].strip(), end='')
        # this will not work if reading input text from stdin!!!
        input()
        #time.sleep(8) 
        print('\t\t\t\t', t2e[1].strip())
        time.sleep(2) 
        print()
    
