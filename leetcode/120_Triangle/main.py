import copy

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        height = len(triangle)
        if height == 0:
            return 0
        list_temp = copy.copy(triangle[height-1])
        for i in range(height-2, -1, -1):
            for j in range(len(triangle[i])-1):
                list_temp[i] = min(list_temp[j], list_temp[j+1]) + triangle[i][j]
        return list_temp[0]




list_test = [1, 2, 3]
for idx in range(len(list_test)-1, -1, -1):
    print(list_test[idx])