import copy

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 1:
            return [1, 1]
        list_result = [1]
        for idx in range(2, rowIndex + 1):
            num_2 = list_result[0]
            for i in range(1, len(list_result)):
                num_1 = num_2
                num_2 = list_result[i]
                list_result[i] = num_1 + num_2
            if idx % 2 == 0:
                list_result.append(num_2 * 2)
        if rowIndex % 2 != 0:
            list_result += copy.copy(list_result)[::-1]
        else:
            list_result += copy.copy(list_result[0:-1])[::-1]
        return list_result

mySolution = Solution()
print(mySolution.getRow(6))
