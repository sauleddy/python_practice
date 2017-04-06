import random
import copy


class Solution(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.nums

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        list_result = list(self.nums)
        len_nums = len(list_result)
        for idx in range(len_nums):
            idx_swap = random.randint(0, len_nums - 1)
            # idx_swap = random.randrange(0, len_nums)
            # print(idx, idx_swap)
            list_result[idx], list_result[idx_swap] = list_result[idx_swap], list_result[idx]
        return list_result

        # Your Solution object will be instantiated and called as such:
        # obj = Solution(nums)
        # param_1 = obj.reset()
        # param_2 = obj.shuffle()
