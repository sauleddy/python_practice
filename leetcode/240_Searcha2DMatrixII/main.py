class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        len_row, len_col = len(matrix), len(matrix[0])
        row_pivot, col_pivot = 0, 0
        while row_pivot < len_row and col_pivot < len_col:
            if matrix[row_pivot][col_pivot] == target:
                return True
            if matrix[row_pivot][col_pivot] > target:
                break
            row_pivot += 1
            col_pivot += 1
        row_left, col_left = row_pivot, col_pivot - 1
        row_up, col_up = row_pivot - 1, col_pivot
        end_left, end_up = False, False
        while end_left is False or end_up is False:
            if end_left is False and row_left < len_row and col_left >= 0:
                if matrix[row_left][col_left] == target:
                    return True
                if matrix[row_left][col_left] > target:
                    col_left -= 1
                else:
                    row_left += 1
            else:
                end_left = True

            if end_up is False and col_up < len_col and row_up >= 0:
                if matrix[row_up][col_up] == target:
                    return True
                if matrix[row_up][col_up] > target:
                    row_up -= 1
                else:
                    col_up += 1
            else:
                end_up = True

        return False
