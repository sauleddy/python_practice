import sys

class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        num_min, num_min2 = sys.maxsize, sys.maxsize
        for idx in range(len(nums)):
            if nums[idx] > num_min2:
                return True
            if nums[idx] <= num_min:
                num_min = nums[idx]
            elif nums[idx] <= num_min2:
                num_min2 = nums[idx]
        return False

print(sys.maxsize)

