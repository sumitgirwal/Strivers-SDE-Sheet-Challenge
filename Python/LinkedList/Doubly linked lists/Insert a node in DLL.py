def addNode(head, pos, data):
    # Code here
    newNode = Node(data)
    curr = head
    for i in range(pos):
        if curr==None:
            return
        curr = curr.next
    
    newNode.next = curr.next
    newNode.prev = curr
    curr.next = newNode
    return 