class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return
        len_row = len(matrix)
        len_col = len(matrix[0])
        row1_zero = False
        for idx_col in range(0, len_col):
            if matrix[0][idx_col] == 0:
                row1_zero = True
        col1_zero = False
        for idx_row in range(0, len_row):
            if matrix[idx_row][0] == 0:
                col1_zero = True

        for idx_row in range(1, len_row):
            for idx_col in range(1, len_col):
                if matrix[idx_row][idx_col] == 0:
                    matrix[0][idx_col] = 0
                    matrix[idx_row][0] = 0
        # print(matrix)
        for idx_row in range(1, len_row):
            if matrix[idx_row][0] == 0:
                for idx_col in range(1, len_col):
                    matrix[idx_row][idx_col] = 0
        for idx_col in range(1, len_col):
            if matrix[0][idx_col] == 0:
                for idx_row in range(1, len_row):
                    matrix[idx_row][idx_col] = 0
        # print(matrix)
        if row1_zero == True:
            for idx_col in range(0, len_col):
                matrix[0][idx_col] = 0
        if col1_zero == True:
            for idx_row in range(0, len_row):
                matrix[idx_row][0] = 0


