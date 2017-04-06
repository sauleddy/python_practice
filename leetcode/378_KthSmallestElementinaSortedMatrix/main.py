from itertools import chain

class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        list_nums = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                list_nums.append(matrix[i][j])
        list_nums = sorted(list_nums)
        return list_nums[k - 1]



