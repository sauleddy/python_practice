# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        deepest = [0]
        self.help(root, deepest)
        return deepest[0]

    def help(self, root, deepest):
        if root is None:
            return 0
        deep_left = self.help(root.left, deepest)
        deep_right = self.help(root.right, deepest)
        deep = deep_left + deep_right
        if deep > deepest[0]:
            deepest[0] = deep
        return max(deep_left, deep_right) + 1

