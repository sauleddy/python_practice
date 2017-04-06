
def square(num):
    return num ** 2

print(square(2))

my_list1 = [num for num in range(11)]
print(map(square, my_list1))
print(list(map(square, my_list1)))


