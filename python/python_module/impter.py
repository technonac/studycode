#!/usr/bin/env python
# -*- coding: utf-8 -*-
import imptee
from imptee import foo, show

show()
imptee.foo = 123
print("foo from impter:", foo)
show()

