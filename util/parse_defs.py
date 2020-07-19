#!/usr/bin/env python3
# intended for parsing out sentences from tagaloglessons definitions files
# reads stdin, writes stdout

import sys
import re
meat = sys.stdin.read()

# toss the beginning through the last "Sentences to Flash Cards":
meat = re.sub(r'.*Sentences to Flash Cards', '', meat, flags=re.DOTALL|re.MULTILINE)

# toss everything from 'Alternate spelling(s): to the end:
meat = re.sub(r'Alternate spelling\(s\):.*', '', meat, flags=re.DOTALL)

# toss everything from "Notice: The Tatoeba sentences" to the end
meat = re.sub(r'Notice: The Tatoeba sentences.*', '', meat, flags=re.DOTALL)

# toss lines with "^ *[.*"
#meat = re.sub(r'^ *\[.*', '', meat, flags=re.MULTILINE)

# toss lines with "user-submitted example sentences", ignoring case:
meat = re.sub(r'^.*user-submitted example sentences.*', '', meat, flags=re.MULTILINE|re.IGNORECASE)

# remove '\r*\n *Tatoeba user-submitted sentence'
meat = re.sub(r'\r*\n *Tatoeba user-submitted sentence', '', meat, flags=re.MULTILINE|re.IGNORECASE)

# toss empty lines:
meat = re.sub(r'^\r*\n', '', meat, flags=re.MULTILINE)

# remove trailing spaces:
meat = re.sub(r'\s+$', '', meat, flags=re.MULTILINE)

# '\xc2\xa0' becomes just '':
#meat = re.sub('\xc2\xa0', '', meat)
# this seems to work, somehow, where the above doesn't..:
meat = re.sub('\xa0', '', meat)

# ' +\t+' becomes just \t:
meat = re.sub(r' +\t+', '\t', meat)

print(meat)
exit()
