class Solution(object):
    turn_player1 = 0
    turn_player2 = 1

    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 0:
            return True
        return self.CanWin(nums, 0, 0, Solution.turn_player1)

    def CanWin(self, nums, sum1, sum2, turn):
        # print(nums, sum1, sum2, turn)
        if len(nums) == 0:
            return sum1 >= sum2
        if len(nums) == 1:
            if turn == Solution.turn_player1:
                return sum1 + nums[0] >= sum2
            else:
                return sum2 + nums[0] > sum1

        if turn == Solution.turn_player1:
            return not self.CanWin(nums[1:],
                                   sum1 + nums[0],
                                   sum2,
                                   Solution.turn_player2) or not self.CanWin(nums[:-1],
                                                                             sum1 + nums[-1],
                                                                             sum2,
                                                                             Solution.turn_player2)
        else:
            return not self.CanWin(nums[1:],
                                   sum1,
                                   sum2 + nums[0],
                                   Solution.turn_player1) or not self.CanWin(nums[:-1],
                                                                             sum1,
                                                                             sum2 + nums[-1],
                                                                             Solution.turn_player1)

# list_test = [1, 2, 3]
# list_slice = list_test[:-1]
# print(list_slice)
# print(list_test)


mySolution = Solution()
print(mySolution.PredictTheWinner([1, 25, 3, 4]))
