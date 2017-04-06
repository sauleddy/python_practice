from collections import Counter
import re


class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        return self.help(s, k)

    def help(self, s, k):
        if len(s) < k:
            return 0
        list_invalid = [key for key, v in Counter(s).items() if v < k]
        # print(list_invalid)
        if len(list_invalid) == 0:
            return len(s)
        # print(list_invalid)
        str_invalid = '|'.join(list_invalid)
        # print(str_invalid)
        list_substring = re.split(str_invalid, s)
        # print(list_substring)
        len_max = 0
        for idx in range(len(list_substring)):
            len_this = self.help(list_substring[idx], k)
            if len_this > len_max:
                len_max = len_this
        return len_max

str_test = 'abcicabh'
print(type(str_test[0]))
list_invalid = [k for k, v in Counter(str_test).items() if v < 2]
print(list_invalid)
str_invalid = '|'.join(list_invalid)
print(str_invalid)
list_split = re.split(str_invalid, str_test)
print(list_split)
