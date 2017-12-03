#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""read and display text file"""
# get file name
fname = raw_input("Enter file name: ")
print("")

# attempt to open file for reading
try:
    fobj = open(fname, 'r')
except IOError, e:
    print("***file open error:", e)
else:  # else子句在try在代码块运行无误时执行
    # display content to the screen
    for eachLine in fobj:
        print eachLine,
    fobj.close()
