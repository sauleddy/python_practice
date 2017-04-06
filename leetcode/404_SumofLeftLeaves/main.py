# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        child_sum = self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
        if root.left is not None and root.left.left is None and root.left.right is None:
            return child_sum + root.left.val
        else:
            return child_sum


