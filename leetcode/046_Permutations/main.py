import copy

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        list_result = []
        self.help(nums, len(nums) - 1, list_result)
        return list_result

    def help(self, nums, pivot, list_result):
        if pivot == 0:
            # print(nums)
            list_result.append(copy.copy(nums))
            return
        for idx in range(pivot + 1):
            nums[idx], nums[pivot] = nums[pivot], nums[idx]
            self.help(nums, pivot - 1, list_result)
            # print(nums)
            nums[idx], nums[pivot] = nums[pivot], nums[idx]


mySolution = Solution()
list_test = [1, 2, 3]
print(mySolution.permute(list_test))

