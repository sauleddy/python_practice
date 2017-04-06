class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        len_s = len(s)
        if len_s <= 1:
            return len_s
        dict_freq = {}
        for idx in range(len_s):
            if s[idx] in dict_freq:
                dict_freq[s[idx]] += 1
            else:
                dict_freq[s[idx]] = 1
        len_longest = 0
        for value in dict_freq.values():
            len_longest += value / 2 * 2
        if len_longest < len_s:
            len_longest += 1
        return len_longest
