# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        list_result = []
        stack_nodes = []
        node_cur = root
        while node_cur is not None:
            if node_cur.left is not None:
                stack_nodes.append(node_cur)
                node_cur = node_cur.left
            elif node_cur.right is not None:
                list_result.append(node_cur.val)
                node_cur = node_cur.right
            else:
                list_result.append(node_cur.val)
                node_cur = None
                while len(stack_nodes) > 0:
                    node_pop = stack_nodes.pop()
                    list_result.append(node_pop.val)
                    if node_pop.right is not None:
                        node_cur = node_pop.right
                        break

        return list_result
