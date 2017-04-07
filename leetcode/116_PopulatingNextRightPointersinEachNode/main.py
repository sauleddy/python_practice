from collections import deque

# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if root is None:
            return
        deque_nodes = deque()
        deque_nodes.append(root)
        num_layer = 1
        while len(deque_nodes) > 0:
            node_this = deque_nodes.popleft()
            if node_this.left is not None:
                deque_nodes.append(node_this.left)
                deque_nodes.append(node_this.right)
            num_layer -= 1
            if num_layer == 0:
                num_layer = len(deque_nodes)
            elif len(deque_nodes) > 0:
                node_this.next = deque_nodes[0]


