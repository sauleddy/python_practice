import random

class Solution(object):
    def __init__(self, nums):
        """

        :type nums: List[int]
        :type numsSize: int
        """
        self.len_nums = len(nums)
        self.nums = nums

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        len_target = 0
        result = -1
        for idx in range(1, self.len_nums):
            if self.nums[idx] == target:
                len_target += 1
                if random.randint(0, len_target - 1) == 0:
                    result = idx
        return result




        # Your Solution object will be instantiated and called as such:
        # obj = Solution(nums)
        # param_1 = obj.pick(target)