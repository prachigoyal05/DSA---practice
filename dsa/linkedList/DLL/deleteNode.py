def delNode(node):

    if node.prev is not None:
        node.prev.next = node.next

    if node.next is not None:
        node.next.prev = node.prev



