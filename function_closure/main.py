
print('closure function')


def closure_func():
    funcs = []
    for idx in range(0, 3):
        def inner_func():
            print('idx=%d' % (idx,))
        funcs.append(inner_func)
    return funcs


my_funcs = closure_func()
for func in my_funcs:
    func()

print('refine closure function')


def closure_func_refined():
    funcs = []
    for idx in range(0, 3):
        def outer_func(num):
            def inner_func():
                print('idx=%d' % (num,))
            return inner_func
        funcs.append(outer_func(idx))
    return funcs


my_funcs = closure_func_refined()
for func in my_funcs:
    func()
