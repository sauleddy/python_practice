class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        len_nums = len(nums)
        if len_nums == 0:
            return False
        if target >= nums[0]:
            for idx in range(len_nums):
                if nums[idx] == target:
                    return True
                elif nums[idx] > target:
                    return False
                elif idx > 0 and nums[idx] < nums[idx - 1]:
                    return False
            return False
        else:
            for idx in range(len_nums - 1, -1, -1):
                if nums[idx] == target:
                    return True
                elif nums[idx] < target:
                    return False
                elif idx < len_nums - 1 and nums[idx] > nums[idx + 1]:
                    return False
            return False