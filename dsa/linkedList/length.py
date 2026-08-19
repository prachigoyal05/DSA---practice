class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def lengthLL(head):
    temp = head
    count = 0

    while temp is not None:
        count+=1
        temp = temp.next

    return count

node1 = Node(10)
node2 = Node(2)
node3 = Node(5)

node1.next = node2
node2.next = node3

head = node1

temp = head

print(lengthLL(head))



