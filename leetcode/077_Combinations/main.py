class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        nums = [num for num in range(1, n + 1)]
        return self.help(nums, 0, len(nums) - 1)

    def help(self, nums, start, end, k):
        if k == 0:
            return []
        if end - start + 1 == k:
            return [nums[idx] for idx in range(start, end+1)]

        list_1 = self.help(nums, start + 1, end, k - 1)
        list_2 = self.help(nums, start + 1, end, k)
        for idx in range(len(list_1)):
            list_1[idx].append(nums[start])
        return list_1 + list_2
