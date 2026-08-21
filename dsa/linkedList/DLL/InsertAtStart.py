def insertNode(head,value):
    newNode = Node(value)
    newNode.next = head
    head = newNode

    if head is not None:
        head.prev = newNode

    return newNode