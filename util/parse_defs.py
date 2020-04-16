#!/usr/bin/env python3
# intended for parsing out sentences from tagaloglessons definitions files
# reads stdin, writes stdout

import sys
import re
dat = sys.stdin.read()
# toss everything through "see a literal translation.*" and from "Join us" to the end
meat = re.sub(r'.*see a literal translation\..*?\n *(.*?)^[^\n]*Notice: The Tatoeba sentences.*', r'\1', dat, flags=re.DOTALL|re.MULTILINE)
# toss occurances of "^ *[.*"
meat = re.sub(r'^ *\[.*', '', meat, flags=re.MULTILINE)
# toss occurances of "^.*ser-submitted.*"
meat = re.sub(r'^.*ser-submitted.*', '', meat, flags=re.MULTILINE)
# toss empty lines:
meat = re.sub(r'(\n *){2,}', '\n', meat)
# toss final empty line:
meat = re.sub(r'\n^$', '', meat, flags=re.MULTILINE)
# fix bug in html that makes " pang" become " pan style.*pangpan>"
meat = re.sub(r' pan style.*pangpan>', ' pang', meat)
print(meat)
exit()
