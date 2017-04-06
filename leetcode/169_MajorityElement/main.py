class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        dict_freq = {}
        threshold = len(nums) / 2
        for idx in range(len(nums)):
            if nums[idx] in dict_freq:
                dict_freq[nums[idx]] += 1
            else:
                dict_freq[nums[idx]] = 1
            if dict_freq[nums[idx]] > threshold:
                result = nums[idx]
                break
        return result
