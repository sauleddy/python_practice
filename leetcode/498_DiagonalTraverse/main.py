class Solution(object):
    up_right = 0
    down_bottom = 1

    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        list_ret = []
        row_size = len(matrix)
        if row_size == 0 or len(matrix[0]) == 0:
            return list_ret
        col_size = len(matrix[0])

        type_now = Solution.up_right
        row_now = 0
        col_now = 0
        while row_now != row_size - 1 or col_now != col_size - 1:
            list_ret.append(matrix[row_now][col_now])
            if type_now == Solution.up_right:
                if row_now - 1 >= 0 and col_now + 1 < col_size:
                    row_now -= 1
                    col_now += 1
                else:
                    if col_now + 1 < col_size:
                        col_now += 1
                    else:
                        row_now += 1
                    type_now = Solution.down_bottom
            else:
                if col_now - 1 >= 0 and row_now + 1 < row_size:
                    row_now += 1
                    col_now -= 1
                else:
                    if row_now + 1 < row_size:
                        row_now += 1
                    else:
                        col_now += 1
                    type_now = Solution.up_right

        list_ret.append(matrix[row_now][col_now])
        return list_ret


mySolution = Solution()
'''
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
'''
matrix = [
    [1, 2],
    [4, 5]
]

print(mySolution.findDiagonalOrder(matrix))

'''
list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(hex(id(list1)))
print(hex(id(list2)))
if list1 == list2:
    print('the same')
'''
