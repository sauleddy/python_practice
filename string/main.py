

print(ord('A'))
print(ord('今'))
print(chr(65))
print(chr(20170))

str_unicode_en = 'This is a string'
bytes_utf8_en = str_unicode_en.encode('utf-8')
print(bytes_utf8_en)
str_unicode_ch = '這是字串'
bytes_utf8_ch = str_unicode_ch.encode('utf-8')
print(bytes_utf8_ch)
print(bytes_utf8_ch.decode('utf-8'))

str_animal = 'cat'
str_sentence = 'This is a %s' % str_animal
print(str_sentence)

