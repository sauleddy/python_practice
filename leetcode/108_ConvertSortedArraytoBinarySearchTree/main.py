# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        self.help(nums, 0, len(nums)-1)

    def help(self, nums, left, right):
        len_valid = right - left + 1
        if len_valid < 0:
            return None
        if len_valid == 0:
            return TreeNode(nums[left])
        idx_mid = left + (len_valid - 1) / 2
        node_this = TreeNode(nums[idx_mid])
        node_this.left = self.help(nums, left, idx_mid - 1)
        node_this.right = self.help(nums, idx_mid + 1, right)
        return node_this


