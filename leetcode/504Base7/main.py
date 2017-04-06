class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return '0'
        str_result = ''
        str_sign = ''
        if num < 0:
            str_sign = '-'
        quotient = abs(num)
        while quotient != 0:
            reminder = quotient % 7
            quotient /= 7
            str_result = str(reminder) + str_result
        str_result = str_sign + str_result
        return str_result
