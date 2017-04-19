import math


class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        while n % 4 == 0:
            n = int(n / 4)
        if n % 8 == 7:
            return 4
        idx = 0
        square = 0
        while square <= n:
            b = int(math.sqrt(n - square))
            if square + b * b == n:
                return int(idx > 0) + int(b > 0)
            idx += 1
            square = idx * idx
        return 3


my_solution = Solution()
print(my_solution.numSquares(12))
