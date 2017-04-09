from collections import Iterable


dict_test = {'name': 'Ed', 'boy': 'Joshua'}
print(isinstance(dict_test, Iterable))

str_test = 'Ed'
print(isinstance(str_test, Iterable))

number = 10
print(isinstance(number, Iterable))

for item in dict_test.items():
    print(item)
