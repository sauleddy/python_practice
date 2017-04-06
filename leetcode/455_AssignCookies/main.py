import my_module

"""
list_test = [1, 3, 5, 2]
# big_than_3 = [idx for idx in range(len(list_test)) if list_test[idx] > 3]
big_than_3 = next((idx for idx in range(len(list_test)) if list_test[idx] > 3), None)
print(big_than_3)
"""

my_solution = my_module.Solution()
print(my_solution.findContentChildren([1, 2, 3], [1, 1]))
