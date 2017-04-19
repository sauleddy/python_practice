# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if root is None:
            return 0
        list_result = [0]
        self.help(root, sum, list_result)
        return list_result[0]

    def help(self, root, sum, list_result):
        if root.val == sum:
            list_result[0] += 1

        if root.left is not None:
            self.pathSum(root.left, sum)
            self.pathSum(root.left, sum - root.val)
        if root.right is not None:
            self.pathSum(root.right, sum)
            self.pathSum(root.right, sum - root.val)