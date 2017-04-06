# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        result = self.help(root)
        return max(result)

    def help(self, root):
        if root is None:
            return 0, 0
        ret_left = self.help(root.left)
        ret_right = self.help(root.right)
        ret_not_include = max(ret_left) + max(ret_right)
        ret_include = root.val + ret_left[0] + ret_right[0]
        # print(root.val, ret_not_include, ret_include)
        return ret_not_include, ret_include
