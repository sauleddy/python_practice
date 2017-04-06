class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        list_return = [1]
        for i in range(1, len(nums)):
            list_return.append(list_return[i - 1] * nums[i - 1])
        total_product = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            list_return[i] *= total_product
            total_product *= nums[i]
        return list_return
