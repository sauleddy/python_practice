
def print_kwargs(**kwargs):
    print('Keyword arguments:', kwargs)


def func_outer(saying):
    def func_inner():
        return 'I am ' + saying
    return func_inner


print_kwargs(name='Ed', id='1234567890')

a = func_outer('Ed')
b = func_outer('Tom')
print(a())
print(b())

def call_function(listNum, func):
    func(listNum[0], listNum[1])

listNum = [1, 2]
call_function(listNum, lambda num1, num2: print(num1 + num2))

print(sum(range(1, 4)))

