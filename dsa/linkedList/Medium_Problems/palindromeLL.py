class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def reverseLL(head):
    temp = head
    prev = None

    while temp is not None:
        front = temp.next
        temp.next = prev
        prev = temp
        temp = front

    return prev

def palindromeLL(head):
    slow = head
    fast = head

    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next

    secondHalf = reverseLL(slow.next)

    first = head
    second = secondHalf

    while second is not None:
        if first.data != second.data:
            return False

        first = first.next
        second = second.next

    return True

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(1)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

head = node1

print(palindromeLL(head))
            
        