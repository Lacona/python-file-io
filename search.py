#! /usr/bin/env python3

import re
#import pdb; pdb.set_trace()

#regex pattern
pattern = r'\w*herit\w*'

#gutenberg = open("origin.txt, 'r')
result = re.compile(pattern, re.IGNORECASE)

list_of_results = []

with open('origin.txt', 'r') as gutenberg:
    with open('matches.txt', 'w') as output:
        index = 0
        for line in gutenberg:
            line = line.strip()
            list = line.split()
            index += 1
            matches = result.search(line)
            if matches:
               output.write(str(index)+"\t"+matches.group(0)+"\n")


