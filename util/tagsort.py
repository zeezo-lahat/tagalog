#!/usr/bin/env python3
'''sort stdin, print to stdout
'''
import sys
#mycharorder = 'AaàáâBbCcDdEeéFfGgHhIiìíîJjKkLlMmNnOoòóôPpQqRrSsTtUuúVvXwXxYyZz'
mychars = (
("A", "a", "à", "á", "â"),
("B", "b"),
("C", "c"),
("D", "d"),
("E", "e", "é"),
("F", "f"),
("G", "g"),
("H", "h"),
("I", "i", "ì", "í", "î"),
("J", "j"),
("K", "k"),
("L", "l"),
("M", "m"),
("N", "n"),
("O", "o", "ò", "ó", "ô"),
("P", "p"),
("Q", "q"),
("R", "r"),
("S", "s"),
("T", "t"),
("U", "u", "ú"),
("V", "v"),
("W", "w"),
("X", "x"),
("Y", "y"),
("Z", "z"),
)
def gettagindex(mystr):
    indexes = []
    for x in mystr:
        letterindex = 0
        got = 999
        for c in mychars:
            if x in c[0]:
                got = letterindex
                break
            else:
                letterindex += 1
        indexes.append(got)
    return indexes
      
assert gettagindex("Ab") < gettagindex("ab")
assert gettagindex("ábot") < gettagindex("ac")
assert gettagindex("a") < gettagindex("B")
assert gettagindex("áb") < gettagindex("ba")
assert gettagindex("ab") < gettagindex("bá")
assert gettagindex("á") < gettagindex("â")
assert gettagindex("â") < gettagindex("B")
assert gettagindex("é") < gettagindex("í")
assert gettagindex("é") < gettagindex("w")
def tcmp(string):
    # if any chars in the input are not in this string, you're screwed..
    sortstr=" !'(),-./;<>AaàáâBbCcDdEeéFfGgHhIiìíîJjKkLlMmNnOoòóôPpQqRrSsTtUuúVvXwXxYyZz’…\n\t"
    r = []
    for c in string:
        try:
            r.append(sortstr.index(c))
        except Exception as e:
            #print('got', e, 'on char: ', c)
            r.append(99)
    return r

lines = sys.stdin.readlines()
lines.sort(key=gettagindex)
for line in lines:
    print(line, end='')

assert tcmp('Bathalà') == tcmp('bathala')
assert tcmp('bathalà', 'bathalA') == 0
assert tcmp('bathalà', 'cathalà') == 1
assert tcmp('Bathalà', 'Bathalàb') == -1
assert tcmp('Poón', 'pOOn') == 0
assert tcmp('abala', 'abalá') == 0
assert tcmp('Báklá', 'baklâ') == 0
assert tcmp('útos', 'utós') == 0

