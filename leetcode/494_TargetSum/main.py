class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        dict_dp = {}
        return self.sumOfQualified(nums, S, 0, dict_dp)

    def sumOfQualified(self, nums, S, start, dict_dp):
        if start == len(nums):
            return S == 0
        if dict_dp.get(start, {}).get(S, 0):
            return dict_dp[start][S]
        res1 = self.sumOfQualified(nums, S - nums[start], start + 1, dict_dp)
        res2 = self.sumOfQualified(nums, S + nums[start], start + 1, dict_dp)
        result = res1 + res2
        dict_dp[start] = {S: result}
        return result


mySolution = Solution()
print(mySolution.findTargetSumWays([1, 1, 1, 1, 1], 3))
