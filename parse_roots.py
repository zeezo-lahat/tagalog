import sys
import re
f = open(sys.argv[1], 'r')
d = f.read()
root = re.sub(r'.*Example words using the Filipino / Tagalog root "(.*?)".*', r'\1', d, flags=re.DOTALL)
meat = re.sub(r'.*Example words using the Filipino / Tagalog root ".*?".*?\n *(.*?)Join us.*', r'\1', d, flags=re.DOTALL)
entries = re.split(r' *\[\d+\]more.*?\]', meat, flags=re.DOTALL)
for i in entries:
    entry = re.sub(r'^\[.*?\]', '', i)
    entry = re.sub(r' *\[\d+\].*', '', entry)
    entry = re.sub(r' *.*?\](.*) *\[\d.*', r'\1', entry)
    entry = re.sub(r'\n', '', entry)
    entry = re.sub(r':', '<' + root + '>', entry)
    entry = re.sub(r'  *', ' ', entry)
    print(entry)
'''
bilhín : [verb] to buy something; * focus on the thing being bought

pambilí : [noun] money that will be used to buy something

mamilí : [verb] to buy; to go shopping; to shop
bilhán : [verb] to buy something for someone (BF) - focus on the
   person being bought for; to buy something somewhere (LF) - focus on
   where something was bought
ibilí : [verb] to buy something for someone (BF); to purchase
   something for someone(BF); to buy with something (e.g., money) (IF)

mabilí : [verb] to be bought; to happen to buy
pinamilí : [noun] purchase; purchased item; items purchased

'''
