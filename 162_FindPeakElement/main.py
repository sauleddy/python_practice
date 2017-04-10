class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for idx in range(1, len(nums)):
            if nums[idx] < nums[idx-1]:
                return idx-1
        return len(nums) - 1