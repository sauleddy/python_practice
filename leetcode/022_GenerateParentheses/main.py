class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        list_result = []
        self.help(n, n, '', list_result)
        return list_result

    def help(self, left, right, str_cur, list_result):
        if left > right:
            return
        if left == 0 and right == 0:
            list_result.append(str_cur)
            return
        if left == 0:
            list_result.append(str_cur + ')' * right)
            return
        print(left, right)
        self.help(left - 1, right, str_cur + '(', list_result)
        self.help(left, right - 1, str_cur + ')', list_result)


mySolution = Solution()
print(mySolution.generateParenthesis(3))



