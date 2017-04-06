from collections import deque

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """


class NestedInteger(object):
    def isInteger(self):
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """

    def getInteger(self):
        """
          @return the single integer that this NestedInteger holds, if it holds a single integer
          Return None if this NestedInteger holds a nested list
          :rtype int
          """

    def getList(self):
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        :rtype List[NestedInteger]
        """


class NestedIterator(object):
    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.deque_nodes = deque(nestedList)
        self.prepareNext()

    def next(self):
        """
        :rtype: int
        """
        result = self.deque_nodes.popleft().getInteger()
        self.prepareNext()
        return result

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.deque_nodes) > 0

    def prepareNext(self):
        if len(self.deque_nodes) == 0:
            return
        if self.deque_nodes[0].isInteger() is True:
            return
        node_cur = self.deque_nodes.popleft().getList()
        for node in node_cur[::-1]:
            if node.isInteger() is True:
                self.deque_nodes.appendleft(node)
            elif len(node.getList()) > 0:
                self.deque_nodes.appendleft(node)
        return self.prepareNext()


list_test = [1, 2, 3]
deque_test = deque(list_test)
while len(deque_test) > 0:
    print(deque_test.popleft())
