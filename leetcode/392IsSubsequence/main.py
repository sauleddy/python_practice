class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s:
            return True
        idx_i = 0
        for i in range(len(t)):
            if t[i] == s[idx_i]:
                idx_i += 1
            if idx_i == len(s):
                return True
        return False
