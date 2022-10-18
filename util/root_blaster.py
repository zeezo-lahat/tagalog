#!/usr/bin/env python3
"""
 given args which are a number of patterns to match against the foo_ affix
 strings in roots.txt, return all the roots and their corresponding matches for
 roots that match each pattern

naaakmâ (akma) naCV_ [adjective] fitted; suited
Akó na namán?! (ako) phr_ [interjection] Why me?; Why does it always have to be me?
akin (ako) conj_ [pronoun] my; mine; me; I
kaawa-awà (awa) ka_rt_rt [adjective] pitiful
umangkát (angkat) _um_ [verb] to import
maangkín (angkin) ma_ [verb] to be able to claim something
Akala mo lang 'yun! (akala) phr_ [interjection] phrase told to someone who supposed something incorrectly; You thought that?!
"""

import sys
import re
import argparse
from collections import defaultdict

rootsfile = 'roots.txt'

parser = argparse.ArgumentParser(
        description='extract matches from roots.txt based on affixes and word types')
parser.add_argument('--affixes', dest='affixes', nargs='+',
                    help='the affixes to match against, eg "mag_ pa_ _an')
parser.add_argument('--wordtype', dest='wordtype', help='specify the word type (eg: verb, adjective)')

args = parser.parse_args()

if args.affixes:
    patternz = args.affixes
else:
    print('I need affixes to match against')
    sys.exit(1)

rootz = defaultdict(list)

with open(rootsfile) as f:
    for line in f:
        m = re.match(r'([^\(]+) \(([^ ]*)\) ([a-zCV]*_*[a-zCV]*_[a-zCV]*) \[([a-z]+)\] (.+)', line)
        if m and m.lastindex == 5:
            word = m.group(1)
            root = m.group(2)
            affix = m.group(3)
            wordtype = m.group(4)
            definition = m.group(5)
            #print('word:', word, 'affix:', affix, 'wordtype:', wordtype)
            if args.wordtype and wordtype != args.wordtype:
                continue
            else:
                rootz[root].append({'word': word, 'type': wordtype, 'affix': affix, 'def': definition})
        else:
            pass # these are the effed up lines in roots.txt

matches = []
for r, r_words in rootz.items():
    #print('  > got root', r)
    # for this root, create a dict having keys for each pattern with value set to false:
    r_matches = dict(zip(patternz, [False]*len(patternz)))
    for p in patternz:
        #print('    > got pattern', p)
        for r_word in r_words:
            #print('       > got word', r_word)
            if r_word['affix'] == p:
                #print('          > got match', r_word)
                r_matches[p] = True

    if not False in r_matches.values():
        matches.append(r)

for root in matches:
    for entry in rootz[root]:
        if entry['affix'] in patternz:
            print(f"{root}:  {entry['word']} - {entry['def']}")
    print('')


'''
rootz = {
    'hintay': [
        {'word': 'maghintay', 'affix': 'mag_', 'def': '[verb] wait'},
        {'word': 'hintayin', 'affix': '_in', 'def': '[verb] wait for stuffz'},
        {'word': 'paghihintay', 'affix': 'pagCV_', 'def': '[noun] waiting'},
        ],
    ...
    }
'''
