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
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        list_sum = self.help(root, sum)
        return map(lambda item: list(reversed(item)), list_sum)

    def help(self, root, sum):
        # print(root.val)
        if root.left is None and root.right is None:
            if root.val == sum:
                return [[root.val]]
            else:
                return []
        list_left, list_right = [], []
        if root.left is not None:
            list_left = self.help(root.left, sum - root.val)
        if root.right is not None:
            list_right = self.help(root.right, sum - root.val)
        list_sum = list_left + list_right
        map(lambda item: item.append(root.val), list_sum)
        return list_sum


list_1 = [1, 2, 3]
print(list(reversed(list_1)))
list_2 = []
list_3 = list_1 + list_2
print(list_3)
