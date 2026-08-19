class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def deleteTail(head):
    if head is None or head.next is None:
        return None

    temp = head

    while temp.next.next is not None:
        temp = temp.next

    temp.next = None

    return head

node1 = Node(10)
node2 = Node(20)
node3 = Node(40)

node1.next = node2
node2.next = node3

head  = node1

head = deleteTail(head)

temp = head

while temp is not None:
    print(temp.data)
    temp = temp.next