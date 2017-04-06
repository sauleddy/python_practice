class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for i in range(32):
            sum_one = 0
            for num in nums:
                sum_one += (num >> i) & 1
            result |= (sum_one % 3) << i
        if result > 0x7FFFFFFF:
            result -= 0x100000000
        return result
