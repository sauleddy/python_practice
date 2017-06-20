from functools import reduce

print('simple map sample')


def square(num):
    return num ** 2


my_list1 = [idx for idx in range(0, 10)]
my_list1_square = map(square, my_list1)
print(list(my_list1_square))


print('simple reduce sample')


def add(x, y):
    return x + y


sum_of_list = reduce(add, my_list1)
print(sum_of_list)


print('simple reduce sample using lambda')
sum_of_list = reduce(lambda x, y: x + y, my_list1)
print(sum_of_list)