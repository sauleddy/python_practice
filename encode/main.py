#!/usr/bin/env python3
# -*- coding: utf-8 -*-

my_str = '你好'
# print(my_str.encode('ascii'))
my_str_utf8 = my_str.encode('utf-8')
print(my_str_utf8)
my_str_unicode = my_str_utf8.decode('utf-8')
print(my_str_unicode)
