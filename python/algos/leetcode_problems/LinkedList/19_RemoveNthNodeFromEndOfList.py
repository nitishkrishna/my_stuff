"""
Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:
Given n will always be valid.
Try to do this in one pass.

"""
__author__ = 'nitish'
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        fast = head
        slow = head
        if fast is None or fast.next is None:
            return None

        while n > 0:
            n -= 1
            fast = fast.next

        if fast is None:
            return head.next

        while fast.next != None:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
        return head

#99.95 percentile