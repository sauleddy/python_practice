class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        len_max = max(len(num1), len(num2))
        num1 = '0' * (len_max - len(num1)) + num1
        num2 = '0' * (len_max - len(num2)) + num2
        str_result = '' * len_max
        carry = 0
        for idx in range(len_max-1, -1, -1):
            sum_this = num1[idx] + num2[idx] + carry
            carry = sum_this / 10
            str_result[idx] = str(sum_this % 10)
        if carry > 0:
            str_result = '1' + str_result
        return str_result