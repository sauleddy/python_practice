
import datetime
import functools


def add_time(func):
    @functools.wraps(func)
    def print_time_log(log):
        log = str(datetime.datetime.now()) + " : " + log
        func(log)
    return print_time_log


@add_time
def print_log(log):
    print(log)


print_log('This is my log.')
print(print_log.__name__)
