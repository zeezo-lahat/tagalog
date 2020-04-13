#!/usr/bin/env python3
# intended for parsing out sentences from tagaloglessons definitions files
# reads stdin, writes stdout

import sys
import re
dat = sys.stdin.read()
# toss everything through "see a literal translation.*" and from "Join us" to the end
#meat = re.sub(r'.*e(.*?)a', r'\1', dat, flags=re.DOTALL)
meat = re.sub(r'.*see a literal translation\..*?\n *(.*?)^[^\n]*Notice: The Tatoeba sentences.*', r'\1', dat, flags=re.DOTALL|re.MULTILINE)
#meat = re.sub(r'.*see a literal translation\..*?\n*(.*?)Join us.*\n', r'\1', dat, flags=re.DOTALL)
#print('1:\n', meat)
#exit()
# toss occurances of "^ *[.*"
meat = re.sub(r'^ *\[.*', '', meat, flags=re.MULTILINE)
#print('2:\n', meat)
# toss occurances of "^.*ser-submitted.*"
meat = re.sub(r'^.*ser-submitted.*', '', meat, flags=re.MULTILINE)
#print('3:\n', meat)
# toss occurances of "^\W*$"
#meat = re.sub(r'^\W*$', '', meat, flags=re.MULTILINE)
#meat = re.sub(r'\W{3,}', '', meat)
# toss empty lines:
meat = re.sub(r'(\n *){2,}', '\n', meat)
# toss final empty line:
meat = re.sub(r'\n^$', '', meat, flags=re.MULTILINE)
#print('4:\n', meat)
# fix bug that makes " pang" become " pan style.*pangpan>"
meat = re.sub(r' pan style.*pangpan>', ' pang', meat)
print(meat)
exit()

'''
entries = re.split(r' *\[\d+\]more\..*?\xbb', meat, flags=re.DOTALL)  # want to split on " *[999]more" up through "\xbb"

for i in entries:
    i = re.sub(r'^\W*\[.*?\]', '', i)  # remove leading [999]
    i = re.sub(r'\n', '', i)  # remove newline
    i = re.sub(r'  *', ' ', i)  # remove multiple spaces
    i = re.sub(r':', '(' + root + ')', i)  # surround with parens
    if len(i) > 1:
        print(i)

   Click/Tap an underline word to see its literal definition Click or tap
   any underlined word to see a literal translation.
   Maníniwalà lang akó kapág nakita ko mismo.
   [41]Play audio #27671 [42]Play audio #27672 [43][loop.svg]
   
   I will only believe it when I see it for myself.
   Ikáw mismo ang sumirà ng pangalan mo.
   [44]Play audio #31592 [45]Play audio #31593 [46][loop.svg]
   
   You yourself ruined your reputation.
   Pumuntá siyá mismo.
   [47]Play audio #33036 [48]Play audio #33037 [49][loop.svg]
   
   He went himself.
   Akó mismo ang pumuntá.
   I myself went.
   Huwág mong bastá ibíbigáy kahit kanino. Ibigáy mo mismo kay Peter.
   Don't just give it to anyone. Give it to Peter personally.
   Join us! We are a free online community for Filipino / Tagalog language

   
   average; colloquial [adverb] commonly; generally; in general; chiefly;
   customarily   [32]more... »
   [33]di-pangkaraniwan : [adjective] unusual; peculiar; extraordinary
   [34]more... »
   [35]pinakakaraniwan : [adjective] commonest; most common   [36]more...
   »
'''
