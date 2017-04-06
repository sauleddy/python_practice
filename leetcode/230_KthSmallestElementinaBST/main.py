# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        list_order = []
        self.help(root, k, list_order)
        return list_order[k - 1]

    def help(self, root, k, list_order):
        if len(list_order) >= k:
            return
        if root is None:
            return
        self.help(root.left, k, list_order)
        list_order.append(root.val)
        self.help(root.right, k, list_order)
