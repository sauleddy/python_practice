
def gen_square_calculator_v1():

    funcs = []
    for i in range(0, 3):
        def square_calculator():
            return i ** 2
        funcs.append(square_calculator)

    return funcs


f11, f12, f13 = gen_square_calculator_v1()
print(f11())
print(f12())
print(f13())


def gen_square_calculator_v2():

    funcs = []
    for i in range(0, 3):
        def func_outer(num):
            def square_calculator():
                return num ** 2
            return square_calculator
        funcs.append(func_outer(i))
    return funcs


f21, f22, f23 = gen_square_calculator_v2()
print(f21())
print(f22())
print(f23())
