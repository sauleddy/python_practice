
def func(a, b, c):
    print(a, b, c)


args = (1, 3, 4)
func(*args)

my_dict = {'b': 1, 'a': 2, 'c': 3}
func(**my_dict)
