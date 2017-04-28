# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root is None:
            return []
        if root.left is None and root.right is None:
            return [str(root.val)]
        list_left, list_right = [], []
        if root.left is not None:
            list_left = self.binaryTreePaths(root.left)
        if root.right is not None:
            list_right = self.binaryTreePaths(root.right)
        list_total = list_left + list_right
        list_total = list(map(lambda x: str(root.val) + '->' + x, list_total))
        return list_total

