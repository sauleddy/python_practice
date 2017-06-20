from collections import Iterable
from collections import Iterator

print('judge if [] is iterable')
print(isinstance([], Iterable))
print('judge if {} is iterable')
print(isinstance({}, Iterable))
print('judge if \'\' is iterable')
print(isinstance('', Iterable))

print('judge if [] is iterator')
print(isinstance([], Iterator))
print('judge if {} is Iterator')
print(isinstance({}, Iterator))
print('judge if \'\' is Iterator')
print(isinstance('', Iterator))

my_list1 = [1, 2, 3]
my_list1_iterator = iter(my_list1)
print(next(my_list1_iterator))
print(next(my_list1_iterator))
print(next(my_list1_iterator))
# print(next(my_list1_iterator))
print('judge if iter(%s) is Iterator' % (my_list1,))
print(isinstance(my_list1_iterator, Iterator))


