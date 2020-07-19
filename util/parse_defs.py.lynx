#!/usr/bin/env python3
# intended for parsing out sentences from tagaloglessons definitions files
# reads stdin, writes stdout

import sys
import re
meat = sys.stdin.read()


# toss everything through "see a literal translation.*" and from "Join us" to the end
#meat = re.sub(r'.*see a literal translation\..*?\n *(.*?)^[^\n]*Notice: The Tatoeba sentences.*', r'\1', dat, flags=re.DOTALL|re.MULTILINE)

# toss everything through the last "Sentences to Flash Cards\n":
meat = re.sub(r'.*Sentences to Flash Cards\n', '', meat, flags=re.DOTALL|re.MULTILINE)

# toss everything 'Alternate spelling(s): to the end:
meat = re.sub(r'Alternate spelling\(s\):.*', '', meat, flags=re.DOTALL)

# toss everything from "Tatoeba Sentence Notice" to the end
meat = re.sub(r'Tatoeba Sentence Notice.*', '', meat, flags=re.DOTALL)

# toss lines with "^ *[.*"
meat = re.sub(r'^ *\[.*', '', meat, flags=re.MULTILINE)

# toss lines with "being fluent in Tagalog."
meat = re.sub(r'^.*being fluent in Tagalog.', '', meat, flags=re.MULTILINE)

# toss lines with "^.*ser-submitted.*"
meat = re.sub(r'^.*ser-submitted.*', '', meat, flags=re.MULTILINE)

# toss empty lines:
#meat = re.sub(r'(\n *){2,}', '\n', meat)
meat = re.sub(r'(\n){2,}', '\n', meat)

# remove leading spaces:
meat = re.sub(r'^ *', '', meat, flags=re.MULTILINE)

# toss final empty line:
meat = re.sub(r'\n^$', '', meat, flags=re.MULTILINE)

# fix bug in html that makes " pang" become " pan style.*pangpan>"
#meat = re.sub(r' pan style.*pangpan>', ' pang', meat)

print(meat)
exit()
