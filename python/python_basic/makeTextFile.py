#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""create a text file"""

import os

ls = os.linesep

# get file name
while True:
    fname = raw_input("Enter a file name: ")
    if os.path.exists(fname):
        print("Error: '%s' is already exists" % fname)
    else:
        break

# get file content lines
all = []
print("\n Enter lines('.' by itself to quit).\n")

# loop until user terminates input
while True:
    entry = raw_input('> ')
    if entry == '.':
        break
    else:
        all.append(entry)

# write lines to file with proper line-ending
fobj = open(fname, 'w')
fobj.writelines(['%s%s' % (x, ls) for x in all])
fobj.close()
print('DONE!')
