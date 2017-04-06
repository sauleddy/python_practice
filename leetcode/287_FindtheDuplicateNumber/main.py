class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len_nums = len(nums)
        low, high = 1, len_nums - 1
        while low <= high:
            num_mid = low + (high - low) / 2
            num_less_mid = 0
            for idx in range(len(nums)):
                if nums[idx] <= num_mid:
                    num_less_mid += 1
            if num_less_mid > num_mid:
                high = num_mid - 1
            else:
                low = num_mid + 1
        return low



