class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        len_nums = len(nums)
        if len_nums == 0:
            return -1
        if target >= nums[0]:
            for idx in range(len_nums):
                if nums[idx] == target:
                    return idx
                elif nums[idx] > target:
                    return -1
                elif idx > 0 and nums[idx] < nums[idx - 1]:
                    return -1
            return -1
        else:
            for idx in range(len_nums - 1, -1, -1):
                if nums[idx] == target:
                    return idx
                elif nums[idx] < target:
                    return -1
                elif idx < len_nums - 1 and nums[idx] > nums[idx + 1]:
                    return -1
            return -1
