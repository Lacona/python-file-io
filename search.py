#! /usr/bin/env python3

import sys
import re

#regex pattern to find all words containing 'herit'
pattern = r'\w*herit\w*'

# results include upper and lower case
result = re.compile(pattern, re.IGNORECASE)

# list of the results
list_of_results = []

# open the gutenberg text and write the results in the output file matches.txt
def matches():
    with open('origin.txt', 'r') as gutenberg:
        with open('matches.txt', 'w') as output:
            index = 0
    
# adding the line numbers and layout of the output
            for line in gutenberg:
                line = line.strip()
                list = line.split()
                index += 1
                matches = result.search(line)
                if matches:
                   output.write(str(index)+"\t"+matches.group(0)+"\n")

if __name__ == '__main__':
    main()
