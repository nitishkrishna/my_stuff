# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = head
        while cur:
            candidate = cur.next
            while candidate and candidate.val == cur.val:
                candidate = candidate.next
            cur.next = candidate
            cur = cur.next
        
        return head

#73.51%
