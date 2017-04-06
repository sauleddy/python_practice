class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g = sorted(g)
        s = sorted(s)
        idx_g = 0
        for i in range(len(s)):
            if idx_g == len(g):
                break
            if s[i] >= g[idx_g]:
                idx_g += 1

        return idx_g
