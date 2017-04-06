

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num <= 9:
            return num
        reminder = num % 9
        if reminder == 0:
            return 9
        return reminder
