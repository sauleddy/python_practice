from collections import deque
import math

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        str_result = ''
        q = deque([root])
        print(str_result)
        while len(q) > 0:
            node_this = q.popleft()
            if node_this is None:
                str_result += '# '
            else:
                str_result += (str(node_this.val) + ' ')
                q.append(node_this.left)
                q.append(node_this.right)
        # print(str_result)
        return str_result

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if len(data) == 0:
            return None
        list_data = data.split()
        list_node = []
        for idx in range(len(list_data)):
            if list_data[idx] == '#':
                list_node.append(None)
            else:
                list_node.append(TreeNode(list_data[idx]))
        # print(list_data)
        len_node = len(list_node)
        idx_child = len_node - 2
        for idx in range(len_node - 1, -1, -1):
            if list_node[idx] is not None:
                list_node[idx].left = list_node[idx_child]
                list_node[idx].right = list_node[idx_child + 1]
                idx_child -= 2
        return list_node[0]

        # Your Codec object will be instantiated and called as such:
        # codec = Codec()
        # codec.deserialize(codec.serialize(root))

# q = deque([1, None, 2])
# print(q.count(None))

list_test = [1, 2, 3, 4]
for idx in range(len(list_test)-1, -1, -1):
    print(list_test[idx])
