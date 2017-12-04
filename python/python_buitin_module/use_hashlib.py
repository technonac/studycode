#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python的hashlib提供了常见的摘要算法，如MD5，SHA1等等。
摘要算法又称哈希算法、散列算法。它通过一个函数，把任意长度的数据转换为一个长度固定的数据串（通常用16进制的字符串表示）。
摘要算法就是通过摘要函数f()对任意长度的数据data计算出固定长度的摘要digest，目的是为了发现原始数据是否被人篡改过。
摘要算法之所以能指出数据是否被篡改过，就是因为摘要函数是一个单向函数，计算f(data)很容易，但通过digest反推data却非常困难。而且，对原始数据做一个bit的修改，都会导致计算出的摘要完全不同。
"""
import hashlib

# MD5是最常见的摘要算法，速度很快，
# 生成结果是固定的128 bit字节，通常用一个32位的16进制字符串表示
m = hashlib.md5()
m.update('hello world!'.encode('utf-8'))
print(m.hexdigest())

# SHA1的结果是160 bit字节，通常用一个40位的16进制字符串表示。
# 比SHA1更安全的算法是SHA256和SHA512，不过越安全的算法不仅越慢，而且摘要长度更长。
s = hashlib.sha1()
s.update('hello world'.encode('utf-8'))
print(s.hexdigest())
