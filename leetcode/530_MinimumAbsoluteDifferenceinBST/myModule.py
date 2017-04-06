
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        l_order = []
        self.in_order(root, l_order)
        diff_min = None
        for i in range(1, len(l_order)):
            diff_abs = l_order[i] - l_order[i-1]
            if diff_min is None:
                diff_min = diff_abs
            else:
                diff_min = min(diff_abs, diff_min)
        return diff_min

    def in_order(self, root, l_order):
        if root is None:
            return None
        self.in_order(root.left, l_order)
        l_order.append(root.val)
        self.in_order(root.right, l_order)


