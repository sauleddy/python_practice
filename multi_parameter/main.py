

def print_multi_values(*param):
    print(param)


print_multi_values(1, 2, 3)
list_test = [4, 5, 6]
print_multi_values(*list_test)


def print_multi_dict_values(**param):
    print(param)


print_multi_dict_values(name='Ed', age=35, title='father')
dict_test = {'name': 'Ed', 'age': 35, 'title': 'father'}
print_multi_dict_values(**dict_test)


def print_city_blood(name, age, *, city, blood):
    print(city, blood)


print_city_blood('Ed', 35, blood='A', city='Taipei')
