class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return []
        nums = sorted(nums)
        dict_duplicate = {}
        list_result = self.help(nums, 0, dict_duplicate)
        return list_result

    def help(self, nums, begin, dict_duplicate):
        if begin == len(nums) - 1:
            list_new = [nums[len(nums) - 1]]
            dict_duplicate[tuple(list_new)] = 1
            return [[], list_new]
        list_ret = self.help(nums, begin + 1, dict_duplicate)
        # print(list_ret)
        for idx in range(len(list_ret)):
            list_new = copy.copy(list_ret[idx])
            list_new.append(nums[begin])
            if dict_duplicate.get(tuple(list_new), 0) == 0:
                dict_duplicate[tuple(list_new)] = 1
                list_ret.append(list_new)
        # print(list_ret)
        return list_ret
