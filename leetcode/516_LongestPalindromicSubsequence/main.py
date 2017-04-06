class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        w, h = len(s), len(s)
        matrix_dp = [[-1 for x in range(w)] for y in range(h)]
        return self.help(s, 0, len(s) - 1, matrix_dp)

    def help(self, s, i, j, matrix_dp):
        if i == j:
            return 1
        if i > j:
            return 0
        if matrix_dp[i][j] != -1:
            return matrix_dp[i][j]

        if s[i] == s[j]:
            matrix_dp[i][j] = self.help(s, i+1, j-1, matrix_dp) + 2
        else:
            long_left = self.help(s, i+1, j, matrix_dp)
            long_right = self.help(s, i, j-1, matrix_dp)
            matrix_dp[i][j] = max(long_left, long_right)
        return matrix_dp[i][j]