class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        list_result = [[0 for i in range(n)] for j in range(n)]
        self.help(0, 0, n, 1, list_result)
        return list_result

    def help(self, x, y, n, num_cur, list_result):
        if n == 1:
            list_result[x, y] = num_cur
            return

        x_cur, y_cur = x, y
        for idx_x in range(x_cur, x + n):
            list_result[idx_x][y_cur] = num_cur
            num_cur += 1
        x_cur = x + n - 1
        y_cur += 1
        for idx_y in range(y_cur, y + n):
            list_result[x_cur][idx_y] = num_cur
            num_cur += 1
        x_cur -= 1
        y_cur = y + n - 1
        for idx_x in range(x_cur, x - 1, -1):
            list_result[idx_x][y_cur] = num_cur
            num_cur += 1
        x_cur = x
        y_cur -= 1
        for idx_y in range(y_cur, y, -1):
            list_result[x_cur][idx_y] = num_cur
            num_cur += 1
        x_cur += 1
        y_cur = y + 1
        n -= 2
        if n >= 1:
            self.help(x_cur, y_cur, n, num_cur, list_result)
