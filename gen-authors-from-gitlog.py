#!/usr/bin/python
#
# Copyright (c) 2010, Sascha Peilicke <saschpe@suse.de>, Novell Inc.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program (see the file COPYING); if not, write to the
# Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA

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
