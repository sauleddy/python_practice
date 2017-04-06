from collections import defaultdict


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dict_dp = defaultdict(lambda: None)
        return self.help(m, n, dict_dp)

    def help(self, m_cur, n_cur, m, n, dict_dp):
        if m_cur > m or n_cur > n:
            return 0
        if m_cur == m and n_cur == n:
            return 1
        if dict_dp[(m_cur, n_cur)] is not None:
            return dict_dp[(m_cur, n_cur)]

        sum_this = self.help(m_cur + 1, n_cur, m, n, dict_dp) + \
            self.help(m_cur, n_cur + 1, m, n, dict_dp)
        dict_dp[(m_cur, n_cur)] = sum_this
        return sum_this
