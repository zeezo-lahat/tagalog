#!/usr/bin/env python3
"""sort Tagalog text by line

   * handles input which includes vowels adorned with pronunciation diacritics,
     plain upper and lower case letters, and all other printable ascii chars
   * reads stdin, print to stdout
   * by default, lines are sorted up to any '\t' char.  override with '-t', eg:
       -t ' ': sort lines up to space char
       -t '': sort full lines
   * two-tiered sort:
       primary: letters of the alphabet
       secondary: letter attributes (uppercase precedes lowercase, accents follow.
       eg: "I", "i", "ì", "í", "î")
   * non-letters precede letters
   * example of sorting order:
   ábot    reach, power, capacity
   abot-kamay      within reach
   ábot ng isip    scope
   abot-tanaw      horizon
   yarì    manufacture; making, constructing
   yarí    this
   yarî    made, made of, finished, ready-made, ready
   yariin  to manufacture, construct
   yáring-kamáy    handmade
"""
import sys

linetermchar = '\t'
if len(sys.argv) > 1:
    if len(sys.argv[1]) == 1:
        linetermchar = sys.argv[1]
        if linetermchar == "X":
            linetermchar = ''
    else:
        raise SystemExit(f'Usage: {sys.argv[0]} [single-char-sort-terminator]'
                '\n  (the line-sort terminator character defaults to tab, "\\t"'
                '\n  the value "X" means "sort the whole line")'
                )

def characterordering():
    """define the character ordering in tiers given by tuples"""
    nonletters = [tuple(c for c in r''' !"#$%&'()*+,-./0123456789:;<=>?@[\]^_''')]
    letters = [
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
    ]
    return nonletters + letters

def getstrindex(mystr: str) -> tuple:
    """map string to two bytearrays to be used as sort key function"""
    allchars = characterordering()
    # initialize empty arrays for this string:
    strcharbytes = bytearray()
    strattrbytes = bytearray()
    for x in mystr:
        if x == linetermchar:
            break
        # default value for chars that we have not enumerated "\xff"
        charbytes = bytearray([255])
        attrbytes = bytearray([255])
        for c in allchars:
            if x in c:
                charindex = allchars.index(c)
                attrindex = c.index(x)
                charbytes = bytearray([charindex])
                attrbytes = bytearray([attrindex])
                break
        strcharbytes += charbytes
        strattrbytes += attrbytes
    return (strcharbytes, strattrbytes)
      
assert getstrindex("Ab") < getstrindex("ab")
assert getstrindex("ábot") < getstrindex("ac")
assert getstrindex("a") < getstrindex("B")
assert getstrindex("áb") < getstrindex("ba")
assert getstrindex("ab") < getstrindex("bá")
assert getstrindex("á") < getstrindex("â")
assert getstrindex("â") < getstrindex("B")
assert getstrindex("é") < getstrindex("í")
assert getstrindex("é") < getstrindex("w")
if linetermchar:
    assert getstrindex(f'yarì{linetermchar}manufacture; making, constructing') < \
       getstrindex(f'yarí{linetermchar}this') < \
       getstrindex(f'yarî{linetermchar}made, made of, finished, ready-made, ready') < \
       getstrindex(f'yariin{linetermchar}to manufacture, construct') < \
       getstrindex(f'yáring-kamáy{linetermchar}handmade')

lines = sys.stdin.readlines()
lines.sort(key=getstrindex)
for line in lines:
    print(line, end='')
