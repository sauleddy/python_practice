class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        len_nums = len(nums)
        if len_nums == 0:
            return 0
        begin, end = 0, len_nums-1
        idx_this = 0
        while begin <= end:
            idx_this = (begin + end) / 2
            if nums[idx_this] == target:
                return idx_this
            elif nums[idx_this] > target:
                end = idx_this - 1
            else:
                begin = idx_this + 1
        if nums[idx_this] > target:
            return idx_this
        else:
            return idx_this + 1

