
import datetime
import functools


def print_log_ex_ex(text):
    def print_log_ex(func):
        def print_all_log(*arg):
            print('begin call %s %s' % (text, func.__name__))
            func(arg[0])
            print('end call')
        return print_all_log
    return print_log_ex


@print_log_ex_ex('execute')
def print_log(*arg):
    print(arg[0])


print_log('Today is not my day.')
