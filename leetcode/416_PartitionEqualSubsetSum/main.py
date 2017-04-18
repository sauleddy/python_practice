from functools import reduce


class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        len_nums = len(nums)
        if len_nums < 2:
            return False
        sum_of_nums = reduce(lambda x, y: x + y, nums)
        if sum_of_nums % 2 != 0:
            return False
        target = sum_of_nums / 2
        dict_dp = {x: False for x in range(target + 1)}
        dict_dp[0] = True
        nums = sorted(nums)
        for i in range(len_nums):
            # dict_dp[nums[i]] = True
            for j in range(target, nums[i] - 1, -1):
                dict_dp[j] = dict_dp[j] or dict_dp[j - nums[i]]
                # print(j, dict_dp[j])
        return dict_dp[target]


my_solution = Solution()
print(my_solution.canPartition([1, 2, 3, 5]))
