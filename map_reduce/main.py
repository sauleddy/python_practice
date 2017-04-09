from functools import reduce


def square(num):
    return num ** 2

print(square(2))

my_list1 = [num for num in range(11)]
print(map(square, my_list1))
print(list(map(square, my_list1)))


def accumulate(x, y):
    print(x, y)
    return x + y

# print(reduce(accumulate, [1, 3, 5]))
print(reduce(lambda x, y: x + y, [1, 3, 5]))



