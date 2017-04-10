import sys

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        dict_dp = {}
        return self.help(grid, (0, 0), dict_dp)

    def help(self, grid, tuple_pos, dict_dp):

        if dict_dp.get(tuple_pos, None) is not None:
            return dict_dp[tuple_pos]
        len_row = len(grid)
        len_col = len(grid[0])
        if tuple_pos[0] >= len_row or tuple_pos[1] >= len_col:
            return sys.maxsize
        if tuple_pos[0] == len_row - 1 and tuple_pos[1] == len_col - 1:
            dict_dp[tuple_pos] = grid[tuple_pos[0]][tuple_pos[1]]
            return grid[tuple_pos[0]][tuple_pos[1]]

        res_right = self.help(grid, (tuple_pos[0], tuple_pos[1] + 1), dict_dp)
        res_down = self.help(grid, (tuple_pos[0] + 1, tuple_pos[1]), dict_dp)
        result = min(res_right, res_down) + grid[tuple_pos[0]][tuple_pos[1]]
        dict_dp[tuple_pos] = result
        return result
