from collections import deque
import copy

class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return []
        dict_duplicate = {}
        list_result = self.help(nums, 0, dict_duplicate)
        list_valid = [list_this for list_this in list_result if len(list_this) >= 2]
        for idx in range(len(list_valid)):
            list_valid[idx].reverse()
        # print(list_valid)
        return list_valid

    def help(self, nums, begin, dict_duplicate):
        if begin == len(nums) - 1:
            return [[], [nums[len(nums) - 1]]]

        list_ret = self.help(nums, begin + 1, dict_duplicate)
        # print(list_ret)
        for idx in range(len(list_ret)):
            if len(list_ret[idx]) == 0 or nums[begin] <= list_ret[idx][len(list_ret[idx]) - 1]:
                list_new = copy.copy(list_ret[idx])
                list_new.append(nums[begin])
                if dict_duplicate.get(tuple(list_new), 0) == 0:
                    dict_duplicate[tuple(list_new)] = 1
                    list_ret.append(list_new)
        # print(list_ret)
        return list_ret


mySolution = Solution()
# mySolution.findSubsequences([4, 6, 7, 7])
mySolution.findSubsequences([4, 3, 2, 1, 1, 1])
