#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print('char to integer')
print(ord('a'))
print('integer to char')
print(chr(97))

print('string to bytes')
my_str = '你好'
# print(my_str.encode('ascii'))
my_str_utf8 = my_str.encode('utf-8')
print(my_str_utf8)
my_str_unicode = my_str_utf8.decode('utf-8')
print(my_str_unicode)

print('format')
print('Hello %s %d %x %f' % ('World', 10, 10, 10.5))


