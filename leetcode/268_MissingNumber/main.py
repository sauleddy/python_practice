class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len_nums = len(nums)
        sum_nums = (len_nums + 1) * len_nums / 2
        for idx in range(len_nums):
            sum_nums -= nums[idx]
        return sum_nums
