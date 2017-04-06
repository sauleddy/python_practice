class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        # print(nums)
        list_num_idx = [(nums[i], i) for i in range(len(nums))]
        list_num_idx = sorted(list_num_idx, key=lambda x: x[0], reverse=True)
        # print(list_num_idx)
        list_return = ['' for i in range(len(nums))]
        for i in range(0, len(list_num_idx)):
            if i <= 2:
                if i == 0:
                    list_return[list_num_idx[0][1]] = 'Gold Medal'
                elif i == 1:
                    list_return[list_num_idx[1][1]] = 'Silver Medal'
                else:
                    list_return[list_num_idx[2][1]] = 'Bronze Medal'
            else:
                list_return[list_num_idx[i][1]] = str(i + 1)
        return list_return
