import sys
import re
f = open(sys.argv[1], 'r')
d = f.read()
root = re.sub(r'.*Example words using the Filipino / Tagalog root "(.*?)".*', r'\1', d, flags=re.DOTALL)
meat = re.sub(r'.*Example words using the Filipino / Tagalog root ".*?".*?\n *(.*?)Join us.*', r'\1', d, flags=re.DOTALL)
print('root:', root)
entries = re.split(r' *\[\d+\]more.*?\]', meat, flags=re.DOTALL)
for i in entries:
    entry = re.sub(r' *.*?\](.*) *\[\d.*', r'\1', i)
    print(entry)
'''
[31]maglinis : [verb] to clean; to clean up   [32]
   [33]linisin : [verb] to clean something; to clean up something; to
      cleanse something   [34]
         [35]malinis : [adjective] clean; pristine; faultless; chaste
            [36]
               [37]linisan : [verb] to clean something; to cleanse something
                  [38]
                     [39]paglilinis : [noun] purification; the act of cleaning   [40]
                        »
                           [41]linis : [noun] cleanliness; neatness; purity   [42]
                              [43]kalilinis : just finished cleaning   [44]
                                 [45]panlinis : [noun] anything used to clean; cleaner   [46]
                                    [47]kalinisan : [noun] cleanliness   [48]
                                       [49]luminis : [verb] to become clean   [50]
                                          [51]magpalinis : [verb] to have someone clean   [52]
                                             [53]tagalinis : [noun] cleaning person   [54]
                                                [55]malinis : [verb] to be able to clean; to happen to clean something
                                                     [56]
                                                        [57]napakalinis : [adjective] very clean   [58]
                                                           [59]pinakamalinis : [adjective] cleanest   [60]

'''
