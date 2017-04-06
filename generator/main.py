
'''
def my_generator(threshold):
    for i in range(threshold):
        yield i


for idx in my_generator(5):
    print(idx)

my_generator = my_generator(2)
print(next(my_generator))
print(next(my_generator))
print(next(my_generator))
'''

g = (x * x for x in range(10))
print(g)
print(next(g))
print(next(g))


def my_generator_loop(threshold):
    i = 1
    while i < threshold:
        i *= 2
        x = yield i
        print(x)


my_generator_loop = my_generator_loop(10)
print(my_generator_loop)
print(next(my_generator_loop))
print(next(my_generator_loop))
# print(next(my_generator_loop))

