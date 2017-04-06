import collections


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        counter_s = collections.Counter(s)
        counter_t = collections.Counter(t)
        return counter_s - counter_t == {} and counter_t - counter_s == {}
