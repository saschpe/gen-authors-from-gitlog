#!/usr/bin/python

import sys

if len(sys.argv) != 2:                  # argument check
    sys.stderr.write("please provide a commit history file containing authors.\n")
    exit(1)

with open(sys.argv[1], 'r') as infile:
    authors = []
    for line in infile:
        if line.find('Author:') != -1:  # asuming Git log here
            authors.append(line.split(":")[1].strip())

    authors = set(authors)              # remove dups
    authors = list(authors)             # make it sortable again
    authors.sort()

    with open('AUTHORS', 'w') as outfile:
        for author in authors:
            outfile.write(author + '\n')
