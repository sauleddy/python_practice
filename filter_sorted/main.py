
print('simple filter sample')


def is_odd(num):
    return num % 2 == 1


my_list1 = [idx for idx in range(0, 10)]
my_list1_filtered = filter(is_odd, my_list1)
print(list(my_list1_filtered))


print('simple sorted sample')


def sort_by_grades(item):
    return item[1]


grades = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
grades_sorted = sorted(grades)
print(grades_sorted)
grades_sorted = sorted(grades, key=sort_by_grades, reverse=True)
print(grades_sorted)
