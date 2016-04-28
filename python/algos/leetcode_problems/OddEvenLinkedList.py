"""
Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example:
Given 1->2->3->4->5->NULL,
return 1->3->5->2->4->NULL.

Note:
The relative order inside both the even and odd groups should remain as it was in the input.
The first node is considered odd, the second node even and so on ...

"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        odd_head = head
        if not head:
            return head
        even_head = head.next
        odd_tail = head
        even_tail = head.next
        odd_cur = odd_head
        even_cur = even_head
        if not head.next:
            return head
        while (odd_cur and even_cur):
            if odd_cur.next and odd_cur.next.next:
                odd_cur = odd_cur.next.next
                odd_tail.next = odd_cur
                odd_tail = odd_tail.next
            else:
                odd_cur = None
            if even_cur.next and even_cur.next.next:
                even_cur = even_cur.next.next
                even_tail.next = even_cur
                even_tail = even_tail.next
            else:
                even_cur = None
                even_tail.next = None
        odd_tail.next = even_head
        return odd_head

#62.92 percentile
