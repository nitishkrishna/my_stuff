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
        save_head = head
        cur_node = head
        removal_candidate = head
        node_before_removal_candidate = head
        for x in range(n-1):
            cur_node = cur_node.next
        if cur_node.next == None:
            new_head = head.next
            return new_head
        while cur_node.next != None:
            node_before_removal_candidate = removal_candidate
            removal_candidate = removal_candidate.next
            cur_node = cur_node.next
        node_before_removal_candidate.next=removal_candidate.next
        return head

#99.50 percentile