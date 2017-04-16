class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dict_dp = {0: 1, 1: 1}
        return self.help(n, dict_dp)

    def help(self, n, dict_dp):
        if dict_dp.get(n, None) is not None:
            return dict_dp[n]
        num_this = self.help(n - 1, dict_dp) + self.help(n - 2, dict_dp)
        dict_dp[n] = num_this
        return num_this
