
# the default value of parameter cannot be mutable


def my_func1(my_list=[]):
    my_list.append('End')
    return my_list


ret_list = my_func1()
print(ret_list)
ret_list = my_func1()
print(ret_list)


# the length of parameter isn't fix
# receive a tuple


def my_func2(*my_list):
    print(my_list)
    for idx in range(len(my_list)):
        print(my_list[idx])


my_func2(1, 2, 3, 4, 5)
list1 = [10, 11, 12]
my_func2(*list1)

# receive a dict


def my_func3(**my_dict):
    print(my_dict)
    for key, value in my_dict.items():
        print('%s=%s' % (key, value))


my_func3(Tom=10, John=20, Jim=30)
dict1 = {'Mon': 1, 'Sun': 0, 'Tue': 2}
my_func3(**dict1)


# retrain the name of parameters, can only pass country={} and city={}

def my_func4(*, country, city):
    print('country=%s, city=%s' % (country, city))


# my_func4(name='Tom', age=50)
my_func4(country='U.S.', city='New York')


def my_func5(*arg, country, city):
    print('arg=%s, country=%s, city=%s' % (arg, country, city))

my_func5('Tom', 50, country='U.S.', city='New York')


def my_func6(country, city):
    print('country=%s, city=%s' % (country, city))

my_func6(city='Taipei', country='Taiwan')
