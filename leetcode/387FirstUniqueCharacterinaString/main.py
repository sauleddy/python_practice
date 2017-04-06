class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return -1
        dict_freq = {}
        for i in range(len(s)):
            if not s[i] in dict_freq:
                dict_freq[s[i]] = [1, i]
            else:
                dict_freq[s[i]][0] += 1
        result = -1
        for list_this in dict_freq.values():
            if list_this[0] == 1 and (result == -1 or list_this[1] < result):
                result = list_this[1]
        return result


my_solution = Solution()
print(my_solution.firstUniqChar('leetcode'))
