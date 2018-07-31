# Given a linked list, rotate the list to the right by k places, where k is non-negative.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return None

        k_counter = k
        length = 0

        if k == 0:
            return head

        fast = head
        slow = head

        while (k_counter > 0 and fast is not None):
            k_counter -= 1
            fast = fast.next
            length += 1

        if fast is None:
            k_counter = k % length
            if k_counter == 0:
                return head
            fast = head
            while (k_counter > 0 and fast is not None):
                k_counter -= 1
                fast = fast.next

        while fast.next != None:
            slow = slow.next
            fast = fast.next

        # Cut off k%n nodes and attach to head
        new_head = slow.next
        fast.next = head
        slow.next = None
        return new_head

    def length(self, head):
        n = 0
        while head is not None:
            n += 1
            head = head.next
        return n

# 29.73
# Find next better solution