# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        node_pre = head.next
        node_cur = node_pre.next
        node_pre.next = head
        head.next = node_cur
        head = node_pre
        while node_cur is None or node_cur.next is None:
            node_pre.next = node_cur.next
            node_cur.next = node_pre.next.next
            node_pre.next.next = node_cur
            node_pre = node_cur
            node_cur = node_cur.next
        return head

