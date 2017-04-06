class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        len_s = len(s)
        if len_s == 0:
            return 0
        result = 0
        for idx in range(len_s):
            num_this = ord(s[idx]) - ord('A') + 1
            result = result * 26 + num_this

        return result

num = ord('A')
print(num)
