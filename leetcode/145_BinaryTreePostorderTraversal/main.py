# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        list_result = []
        list_node = [root]
        node_cur = root
        while len(list_node) > 0:
            if node_cur.left is not None:
                list_node.append(node_cur.left)
                node_cur = node_cur.left
            else:
                list_result.append(node_cur.val)
                list_node.pop()
                while len(list_node) > 0:
                    node_parent = list_node[len(list_node)-1]
                    if node_parent.left == node_cur:
                        if node_parent.right is not None:
                            list_node.append(node_parent.right)
                            node_cur = node_parent.right
                            break
                    list_result.append(node_parent.val)
                    node_cur = list_node.pop()

        return list_result





