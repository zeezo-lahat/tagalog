import sys
import re
f = open(sys.argv[1], 'r')
d = f.read()
root = re.sub(r'.*Example words using the Filipino / Tagalog root "(.*?)".*', r'\1', d, flags=re.DOTALL)
meat = re.sub(r'.*Example words using the Filipino / Tagalog root ".*?".*?\n *(.*?)Join us.*', r'\1', d, flags=re.DOTALL)
#entries = re.split(r' *\[\d+\]more.*?[\xbb\]]', meat, flags=re.DOTALL)  # want to split on " *[999]more" up through either "]" or "\xbb"
#entries = re.split(r' *\[\d+\]more.*?\]', meat, flags=re.DOTALL)
entries = re.split(r' *\[\d+\]more\..*?\xbb', meat, flags=re.DOTALL)  # want to split on " *[999]more" up through "\xbb"
for i in entries:
    i = re.sub(r'^\W*\[.*?\]', '', i)  # remove leading [999]
    i = re.sub(r'\n', '', i)  # remove newline
    i = re.sub(r'  *', ' ', i)  # remove multiple spaces
    i = re.sub(r':', '(' + root + ')', i)  # surround with parens
    if len(i) > 1:
        print(i)

'''
[31]karaniwan : [adjective] common; usual; widespread; habitual;
   average; colloquial [adverb] commonly; generally; in general; chiefly;
   customarily   [32]more... »
   [33]di-pangkaraniwan : [adjective] unusual; peculiar; extraordinary
   [34]more... »
   [35]pinakakaraniwan : [adjective] commonest; most common   [36]more...
   »

>>  bumilí : [verb] to buy; to purchase
>>  bilhín : [verb] to buy something; * focus on the thing being bought

>>  pambilí : [noun] money that will be used to buy something

>>  mamilí : [verb] to buy; to go shopping; to shop
>>  bilhán : [verb] to buy something for someone (BF) - focus on the
   person being bought for; to buy something somewhere (LF) - focus on
   where something was bought
>>  ibilí : [verb] to buy something for someone (BF); to purchase
   something for someone(BF); to buy with something (e.g., money) (IF)

>>  mabilí : [verb] to be bought; to happen to buy
>>  pinamilí : [noun] purchase; purchased item; items purchased

>>  mamimili : [noun] customer; client; buyer; consumer
>>  bilihin : [noun] items for sale; merchandise; goods
>>  makabilí : [verb] to be able to buy
>>  magbilí : [verb] to sell; to deal
>>  salaysáy : [noun] narration; story; version; statement; testimony;
   account; claim; assertion; deposition
>>  isalaysáy : [verb] to tell a story about something; to give a
   statement about something; * focus on the thing being told

>>  magsalaysáy : [verb] to tell; to tell a story; to recount

>>  tagapagsalaysáy : [noun] narrator
>>  pagsasalaysáy : [noun] narration; story; version; statement
   [40]more... »

[31]salaysáy : [noun] narration; story; version; statement; testimony;
   account; claim; assertion; deposition   [32]more... »
   [33]isalaysáy : [verb] to tell a story about something; to give a
   statement about something; * focus on the thing being told
   [34]more... »
   [35]magsalaysáy : [verb] to tell; to tell a story; to recount
   [36]more... »
   [37]tagapagsalaysáy : [noun] narrator   [38]more... »
   [39]pagsasalaysáy : [noun] narration; story; version; statement
   [40]more... »

>>  bumilí : [verb] to buy; to purchase
>>  bilhín : [verb] to buy something; * focus on the thing being bought

>>  pambilí : [noun] money that will be used to buy something

>>  mamilí : [verb] to buy; to go shopping; to shop
>>  bilhán : [verb] to buy something for someone (BF) - focus on the
   person being bought for; to buy something somewhere (LF) - focus on
   where something was bought
>>  ibilí : [verb] to buy something for someone (BF); to purchase
   something for someone(BF); to buy with something (e.g., money) (IF)

>>  mabilí : [verb] to be bought; to happen to buy
>>  pinamilí : [noun] purchase; purchased item; items purchased

>>  mamimili : [noun] customer; client; buyer; consumer
>>  bilihin : [noun] items for sale; merchandise; goods
>>  makabilí : [verb] to be able to buy
>>  magbilí : [verb] to sell; to deal
'''
