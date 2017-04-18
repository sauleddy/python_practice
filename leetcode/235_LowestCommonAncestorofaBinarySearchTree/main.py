# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # print(p.val, q.val)
        num_min = min(p.val, q.val)
        num_max = max(p.val, q.val)
        return self.help(root, num_min, num_max)

    def help(self, root, num_min, num_max):
        if root is None:
            return None
        # print(num_min, root.val, num_max)
        if num_min <= root.val <= num_max:
            return root
        print(num_min, root.val, num_max)
        if root.val > num_max:
            return self.help(root.left, num_min, num_max)
        else:
            return self.help(root.right, num_min, num_max)



num1 = 2
num2 = 1
num3 = 0
if num2 <= num3 <= num1:
    print('valid')

