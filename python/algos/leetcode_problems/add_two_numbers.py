# You are given two linked lists representing two non-negative numbers.
# The digits are stored in reverse order and each of their nodes contain a single digit.
# Add the two numbers and return it as a linked list.

import os
import sys
cur_dir = os.path.dirname(__file__)
sys_path_dir = os.path.join(cur_dir, '../../../')
sys.path.append(sys_path_dir)
from python.tools.DataStructures.list import ListNode
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode(0)
        cur_node = result
        carry_val = 0
        while l1 or l2:
            next_node = ListNode(0)
            if l1 == None:
                cur_node.val = l2.val
            elif l2 == None:
                cur_node.val = l1.val
            else:
              cur_node.val = l1.val + l2.val
            if carry_val > 0:
                cur_node.val += carry_val
            carry_val = 0
            if cur_node.val >= 10:
                cur_node.val -= 10
                carry_val = 1
            if l1!=None:
                l1 = l1.next
            if l2!=None:
                l2 = l2.next
            cur_node.next = (None if l1 == None and l2 == None and carry_val == 0 else next_node)
            cur_node = cur_node.next
        if carry_val != 0:
            cur_node.val += carry_val
            cur_node.next = None
        return result

# 66.02 percentile