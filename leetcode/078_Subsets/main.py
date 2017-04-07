class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        list_result = []
        self.help(nums, 0, len(nums) - 1, list_result)
        return list_result

    def help(self, nums, start, end, list_result):
        if start == end:
            list_result.append([])
            list_result.append([nums[start]])
            return

        self.help(nums, start + 1, end, list_result)
        list_copy = copy.deepcopy(list_result)
        for idx in range(len(list_copy)):
            list_copy[idx].append(nums[start])
        list_result += list_copy


list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(list1 + list2)