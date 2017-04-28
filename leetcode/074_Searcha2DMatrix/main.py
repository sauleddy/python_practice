class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        len_row = len(matrix)
        if len_row == 0 or len(matrix[0]) == 0:
            return False
        begin_idx, end_idx = 0, len_row - 1
        row_idx = int((begin_idx + end_idx) / 2)
        while begin_idx <= end_idx:
            if matrix[row_idx][0] <= target <= matrix[row_idx][-1]:
                break
            elif matrix[row_idx][0] > target:
                end_idx = row_idx - 1
            else:
                begin_idx = row_idx + 1
            row_idx = int((begin_idx + end_idx) / 2)
        print(row_idx)
        if begin_idx > end_idx:
            return False
        len_col = len(matrix[row_idx])
        begin_idx, end_idx = 0, len_col - 1
        col_idx = int((begin_idx + end_idx) / 2)
        while begin_idx <= end_idx:
            if matrix[row_idx][col_idx] == target:
                return True
            elif matrix[row_idx][col_idx] > target:
                end_idx = col_idx - 1
            else:
                begin_idx = col_idx + 1
            col_idx = int((begin_idx + end_idx) / 2)
        return False


my_solution = Solution()
print(my_solution.searchMatrix(
    [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 3))
