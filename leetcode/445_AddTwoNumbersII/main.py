# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        list_head = ListNode(0)
        list1, list2 = [], []
        while l1 is not None:
            list1.append(l1.val)
            l1 = l1.next
        while l2 is not None:
            list2.append(l2.val)
            l2 = l2.next
        len_list1 = len(list1)
        len_list2 = len(list2)
        idx1 = len_list1 - 1
        idx2 = len_list2 - 1
        carry = 0
        while idx1 >= 0 or idx2 >= 0:
            sum_this = carry
            if list1:
                sum_this += list1.pop()
            if list2:
                sum_this += list2.pop()
            list_this = ListNode(sum_this % 10)
            list_this.next = list_head.next
            list_head.next = list_this
            carry = sum_this / 10
            idx1 -= 1
            idx2 -= 1
        if carry == 0:
            list_head = list_head.next
        else:
            list_head.val = carry
        return list_head

