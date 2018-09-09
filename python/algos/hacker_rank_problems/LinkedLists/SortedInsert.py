def sortedInsert(head, data):
    node = DoublyLinkedListNode(data)
    cur = head
    
    while(cur.data<data and cur.next is not None):
        cur = cur.next
    
    if cur.next is None and cur.data < data:
        node.prev = cur
        cur.next = node
        return head
    
    prev = cur.prev
    node.prev = prev
    if prev is not None:
        prev.next = node
    else:
        head = node
    node.next = cur
    
    return head
