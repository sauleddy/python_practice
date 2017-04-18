class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        dict_history = {n: 1}
        sum_of_square = n
        while sum_of_square != 1:
            temp = sum_of_square
            sum_of_square = 0
            while temp > 0:
                remainder = temp % 10
                sum_of_square += remainder * remainder
                temp = int(temp / 10)
            print(sum_of_square)
            if dict_history.get(sum_of_square, 0) == 1:
                return False
            dict_history[sum_of_square] = 1
        return True

my_solution = Solution()
print(my_solution.isHappy(19))


