import functools


print(int('10', 2))

int2 = functools.partial(int, base=2)
print(int2('10'))
print(int2('10', base=16))




