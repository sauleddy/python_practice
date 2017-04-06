import math

class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return n
        idx = 1
        while idx ** 2 <= n:
            idx += 1
        return idx - 1