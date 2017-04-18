import math

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        num = math.log(n, 10) / math.log(3, 10)
        print(num)
        print(round(num))
        print(abs(num - round(num)))
        return abs(num - round(num)) < 0.0000000001


my_solution = Solution()
print(my_solution.isPowerOfThree(14348906))
# print(math.log(8, 2))
