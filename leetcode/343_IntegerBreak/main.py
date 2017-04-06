class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        dict_ret = {2: 1, 3: 2, 4: 4}
        if 2 <= n <= 4:
            return dict_ret[n]
        quotient = n / 3
        remainder = n % 3
        if remainder == 0:
            remainder += 1
        elif remainder == 1:
            remainder += 3
            quotient -= 1
        product = 3 ** quotient * remainder
        return product
