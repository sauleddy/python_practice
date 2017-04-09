class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        self.help(matrix, 0, 0, len(matrix))

    def help(self, matrix, x, y, n):
        if n <= 1:
            return
        for idx in range(n - 1):
            x_cur, y_cur = 0, idx
            num_temp = matrix[x_cur + x][y_cur + y]
            x_next, y_next = n - y_cur - 1, x_cur
            matrix[x_cur + x][y_cur + y] = matrix[x_next + x][y_next + y]
            x_cur, y_cur = x_next, y_next
            x_next, y_next = n - 1, x_cur
            matrix[x_cur + x][y_cur + y] = matrix[x_next + x][y_next + y]
            x_cur, y_cur = x_next, y_next
            x_next, y_next = n - y_cur - 1, x_cur
            matrix[x_cur + x][y_cur + y] = matrix[x_next + x][y_next + y]
            matrix[x_next + x][y_next + y] = num_temp

        self.help(matrix, x + 1, y + 1, n - 2)
