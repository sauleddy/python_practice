

print(list(filter(lambda x: x >= 3, [1, 2, 3, 4, 5])))


def sort_func(num):
    return -num


print(sorted([1, 2, 3, 4, 5], key=sort_func, reverse=True))
