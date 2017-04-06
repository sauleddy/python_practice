from collections import deque

# Definition for a  binary tree node
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.deque_order = deque()
        self.help(root, self.deque_order)

    def help(self, root, deque_order):
        if root is None:
            return
        self.help(root.left, deque_order)
        deque_order.append(root.val)
        self.help(root.right, deque_order)

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.deque_order) > 0

    def next(self):
        """
        :rtype: int
        """
        return self.deque_order.popleft()


        # Your BSTIterator will be called like this:
        # i, v = BSTIterator(root), []
        # while i.hasNext(): v.append(i.next())