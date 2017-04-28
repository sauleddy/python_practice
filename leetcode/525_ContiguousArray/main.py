from collections import Counter


class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict_sum_idx = {0: -1}
        result, num_sum = 0, 0
        for idx in range(len(nums)):
            num_sum += 1 if nums[idx] == 1 else -1
            if dict_sum_idx.get(num_sum, None) is not None:
                result = max(result, idx - dict_sum_idx[num_sum])
            else:
                dict_sum_idx[num_sum] = idx
        return result

# list_test = [0, 1, 1, 0]
# print(Counter(list_test))
num1 = 10
num2 = 20
print(num1+100 if num1 == 11 else num1-100)

