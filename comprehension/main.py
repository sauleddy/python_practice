
print('generate list using comprehension')
my_list1 = list(range(1, 10))
print(my_list1)

print('generate list 1x1 2x2... using comprehension')
my_list2 = [(idx, idx) for idx in range(1, 10) if idx % 2 == 0]
print(my_list2)

print('generate list permutation of \'ABC\' and \'DEF\' using comprehension')
my_list3 = [m + n for m in 'ABC' for n in 'DEF']
print(my_list3)

print('generate list from dict key and value using comprehension')
my_dict1 = {'Tom': 50, 'John': 80, 'Tim': 100}
my_list4 = ['%s = %d' % (k, v) for k, v in my_dict1.items()]
print(my_list4)

