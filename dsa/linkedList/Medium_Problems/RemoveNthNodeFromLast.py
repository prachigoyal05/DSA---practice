class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def removeNode(head,N):
    slow = head
    fast = head

    for i in range(N):
        fast = fast.next

    if fast is None:
        return head.next

    while fast.next is not None:
        slow = slow.next
        fast = fast.next

    slow.next = slow.next.next

    return head

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

head = node1

# Remove 2nd node from the end
head = removeNode(head, 5)


# Print Linked List
temp = head

while temp is not None:
    print(temp.data, end=" ")
    temp = temp.next




