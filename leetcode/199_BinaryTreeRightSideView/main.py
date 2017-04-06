from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        list_result = []
        deque_nodes = deque()
        deque_nodes.append(root)
        num_layer = 1
        while len(deque_nodes > 0):
            node_this = deque_nodes.popleft()
            if node_this.left is not None:
                deque_nodes.append(node_this.left)
            if node_this.right is not None:
                deque_nodes.append(node_this.right)
            num_layer -= 1
            if num_layer == 0:
                list_result.append(node_this.val)
                num_layer = len(deque_nodes)
        return list_result



