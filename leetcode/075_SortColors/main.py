class Solution(object):
    def help(self, nums, idx_L, idx_R, target):
        while True:
            while nums[idx_L] == target:
                idx_L += 1
                if idx_L >= len(nums):
                    return None
            while nums[idx_R] != target:
                idx_R -= 1
                if idx_R < 0:
                    return None
            # print(idx_L, idx_R)
            if idx_L < idx_R:
                nums[idx_L], nums[idx_R] = nums[idx_R], nums[idx_L]
            else:
                return idx_L

    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        idx_left = self.help(nums, 0, len(nums) - 1, 0)
        if idx_left is None:
            idx_left = 0
        self.help(nums, idx_left, len(nums) - 1, 1)

mySolution = Solution()
list_test = [1, 2, 1, 0, 0, 2]
mySolution.sortColors(list_test)
print(list_test)

