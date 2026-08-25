class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def reverseLL(head):
    temp = head
    prev = None

    while temp is not None:
        front = temp.next
        temp.next = prev #this will reverse the list
        prev = temp #shifting prev to the current node
        temp = front #shifting temp to the next node

    return prev