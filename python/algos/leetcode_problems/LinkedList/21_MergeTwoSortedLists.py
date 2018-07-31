# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        new_head = ListNode(-1)
        cur = new_head
        l1_cur = l1
        l2_cur = l2
        
        while (l1_cur is not None and l2_cur is not None):
            if(l1_cur.val<=l2_cur.val):
                cur.next = l1_cur
                l1_cur = l1_cur.next
            else:
                cur.next = l2_cur
                l2_cur = l2_cur.next
            
            cur = cur.next
        
        if l1_cur is None:
            cur.next = l2_cur
        else:
            cur.next = l1_cur
        
        return new_head.next

#93.64%
