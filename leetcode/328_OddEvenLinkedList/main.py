# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head
        node_head_even = ListNode(0)
        node_cur_odd = head
        node_cur_even = node_head_even
        while node_cur_odd.next is not None:
            node_cur_even.next = node_cur_odd.next
            node_cur_odd.next = node_cur_even.next.next
            node_cur_even = node_cur_even.next
            node_cur_even.next = None
            if node_cur_odd.next is None:
                break
            node_cur_odd = node_cur_odd.next
        node_cur_odd.next = node_head_even.next
        return head
