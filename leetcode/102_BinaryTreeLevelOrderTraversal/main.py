from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        list_result = []
        deque_nodes = deque()
        deque_nodes.append(root)
        num_layer = 1
        list_layer = []
        while len(deque_nodes) > 0:
            node_this = deque_nodes.popleft()
            if node_this.left is not None:
                deque_nodes.append(node_this.left)
            if node_this.right is not None:
                deque_nodes.append(node_this.right)
            list_layer.append(node_this.val)
            num_layer -= 1
            if num_layer == 0:
                num_layer = len(deque_nodes)
            else:
                list_result.append(list_layer)
                list_layer = []
        return list_result
