'''read stdin, print each char once, in order of appearance'''

import sys
# if any chars in the input are not in this string, boom
sortstr=" !'(),-./;<>BEIPUaàáâbcdeéfghiìíîjklmnoòóôprstuúvwxy’…\n\t"
lines = []
for line in sys.stdin.readline():
    lines.append(line)

lines.sort(key=lambda x: sortstr.index(x))
print(lines)
