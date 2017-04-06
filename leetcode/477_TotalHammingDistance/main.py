class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        distance = 0
        if len(nums) <= 1:
            return distance
        for idx_bit in range(0, 32):
            oper = 1 << idx_bit
            sum_of_one = 0
            for idx in range(len(nums)):
                if nums[idx] & oper != 0:
                    sum_of_one += 1
            distance += sum_of_one * (len(nums) - sum_of_one)

        return distance

my_solution = Solution()
print(my_solution.totalHammingDistance([4, 12, 2]))
