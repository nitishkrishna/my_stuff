class ListNode(object):
    def __init__(self, x=None):
        self.val = x
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = ListNode()

    def append(self, value):
        new_node = ListNode(value)
        cur_node = self.head
        while cur_node.next is not None:
            cur_node = cur_node.next
        cur_node.next = new_node


class DoublyLinkedNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        self.prev = None