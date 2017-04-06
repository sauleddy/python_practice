class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dict_dp = {}
        return self.help(nums, target, dict_dp)

    def help(self, nums, target, dict_dp):
        if target == 0:
            return 1
        if target < 0:
            return 0
        if dict_dp.get(target, -1) != -1:
            return dict_dp[target]

        count = 0
        for num in nums:
            count += self.help(nums, target - num, dict_dp)
        dict_dp[target] = count
        return count