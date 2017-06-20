from collections import Iterable

# judge if the variable is iterable

print('if dict iterable')
dict_test = {'name': 'Ed', 'boy': 'Joshua'}
print(isinstance(dict_test, Iterable))

print('if string iterable')
str_test = 'Ed'
print(isinstance(str_test, Iterable))

print('if number iterable')
number = 10
print(isinstance(number, Iterable))

my_list = ['A', 'B', 'C']
print('enumerate list %s' % (my_list,))
for i, value in enumerate(my_list):
    print('%d=%s' % (i, value))

print('enumerate dict %s' % (dict_test,))
for i, key in enumerate(dict_test):
    print('%d=%s' % (i, key))

print('for item in dict_test.items() %s' % (dict_test,))
for item in dict_test.items():
    print(item)

my_tuple_list = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
print('for item in dict_test.items() %s' % (my_tuple_list,))
for x, y, z in my_tuple_list:
    print(x, y, z)
