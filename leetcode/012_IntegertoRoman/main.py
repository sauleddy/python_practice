class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        list_number = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
        list_number = list_number[::-1]
        dict_roman = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', \
                      90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
        str_result = ''
        while num > 0:
            matches = next(n for n in list_number if n <= num)
            print(matches)
            str_result += dict_roman[matches]
            num -= matches
        return str_result

mySolution = Solution()
print(mySolution.intToRoman(1900))
