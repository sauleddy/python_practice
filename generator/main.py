import sys

print('simple generator')
my_generator = (idx for idx in range(1, 4))
for i in my_generator:
    print(i)

print('fabonacci generator')


def fabonacci_gen():
    last_values = [1, 1]
    for idx in range(0, 10):
        this_value = last_values[0] + last_values[1]
        last_values[0] = last_values[1]
        last_values[1] = this_value
        yield this_value


for i in fabonacci_gen():
    print(i)

# my_generator = fabonacci_gen()
# print(next(my_generator))
# print(next(my_generator))
# print(next(my_generator))


# g = (x * x for x in range(10))
# print(g)
# print(next(g))
# print(next(g))


def my_generator_loop(threshold):
    i = 1
    while i < threshold:
        i *= 2
        yield i
        # print(x)


my_generator_loop = my_generator_loop(5)
try:
    print(my_generator_loop)
    print(next(my_generator_loop))
    print(next(my_generator_loop))
    print(next(my_generator_loop))
    print(next(my_generator_loop))
except StopIteration:
    print(StopIteration.args, StopIteration.value)
finally:
    print('in finalize')
