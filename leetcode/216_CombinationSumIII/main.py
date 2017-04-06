class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        list_nums = [num for num in range(1, 10)]
        list_result = []
        self.help(k, n, 0, len(list_nums) - 1, list_nums, list_result)
        return list_result

    def help(self, k, n, begin, pivot, list_nums, list_result):
        if k == 1:
            # print(list_nums)
            if n in list_nums[begin:pivot + 1]:
                list_this = [n] + list_nums[pivot + 1:]
                list_result.append(list_this)

        for idx in range(begin, pivot + 1):
            if list_nums[idx] < n:
                list_nums[idx], list_nums[pivot] = list_nums[pivot], list_nums[idx]
                self.help(
                    k - 1,
                    n - list_nums[pivot],
                    idx,
                    pivot - 1,
                    list_nums,
                    list_result)
                list_nums[idx], list_nums[pivot] = list_nums[pivot], list_nums[idx]


mySolution = Solution()
print(mySolution.combinationSum3(3, 15))
