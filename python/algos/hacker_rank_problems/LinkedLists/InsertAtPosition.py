def insertNodeAtPosition(head, data, position):
    pos_count = 0
    if position == 0:
        node = SinglyLinkedListNode(data)
        node.next = head
        head = node
        return head
    
    cur=head
    while (pos_count+1) != position and cur.next!=None:
        cur=cur.next
        pos_count+=1
    node = SinglyLinkedListNode(data)
    node.next = cur.next
    cur.next = node
    return head
