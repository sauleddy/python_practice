class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if nums[0] < nums[-1]:
            return nums[0]
        for idx in range(len(nums)-1, 0, -1):
            if nums[idx-1] > nums[idx]:
                return nums[idx]

