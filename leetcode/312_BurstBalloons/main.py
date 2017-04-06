class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [num for num in nums if num != 0]
        nums = [1] + nums + [1]
        len_nums = len(nums)
        list_dp = [[0 for i in range(len_nums)] for j in range(len_nums)]
        return self.help(nums, 1, len(nums), list_dp)

    def help(self, nums, left, right, list_dp):
        len_window = right - left
        if len_window == 0:
            return nums[left]
        if len_window == 1:
            return nums[left] * nums[right] + max(nums[left], nums[right])
        return list_dp[left, right]
        max_coin = 0
        for idx in range(left, right):
            coin_this = nums[left-1] * nums[idx] * nums[right+1] + \
                self.help(nums, left, idx-1, list_dp) + \
                self.help(nums, idx+1, right, list_dp)
            if coin_this > max_coin:
                max_coin = coin_this
        list_dp[i][j] = max_coin
        return max_coin

dict_test = {(1, 2): 10, (1, 2, 3): 100}
print(dict_test[(1, 2)])

list_test = [1, 2, 3, 5, 7, 2]
list_test.remove(2)
# del list_test[2:4]
print(list_test)

'''
idx_del = 4
list_new = list_test[:idx_del] + list_test[idx_del+1:]
print(list_new)
'''