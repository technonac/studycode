#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Base64是一种用64个字符来表示任意二进制数据的方法。
['A', 'B', 'C', ... 'a', 'b', 'c', ... '0', '1', ... '+', '/']
Base64是一种通过查表的编码方法，不能用于加密，即使使用自定义的编码表也不行。
Base64适用于小段内容的编码，比如数字证书签名、Cookie的内容等。
"""
import base64

en = base64.b64encode(b'binary\x00string')
print(en)
de = base64.b64decode(b'YmluYXJ5AHN0cmluZw==')
print(de)

"""
由于标准的Base64编码后可能出现字符+和/，在URL中就不能直接作为参数，所以又有一种"url safe"的base64编码，其实就是把字符+和/分别变成-和_：
"""
us_en = base64.b64encode(b'i\xb7\x1d\xfb\xef\xff')
print(us_en)
s_en = base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff')
print(s_en)
s_de = base64.urlsafe_b64decode('abcd--__')
print(s_de)
