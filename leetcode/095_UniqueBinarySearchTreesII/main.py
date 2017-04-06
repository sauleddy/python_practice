# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        list_nums = [num + 1 for num in range(n)]
        return self.help(list_nums)

    def help(self, list_nums):
        if len(list_nums) == 0:
            return [None]
        if len(list_nums) == 1:
            return [TreeNode(list_nums[0])]

        list_tree = []
        for idx in range(len(list_nums)):
            trees_left = self.help(list_nums[:idx])
            trees_right = self.help(list_nums[idx + 1:])
            for idx_left in range(len(trees_left)):
                for idx_right in range(len(trees_right)):
                    node_this = TreeNode(list_nums[idx])
                    node_this.left = trees_left[idx_left]
                    node_this.right = trees_right[idx_right]
                    list_tree.append(node_this)
        return list_tree

# list_test = [1, 2, 3]
# print(list_test[3:])

