class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def insertAtHead(head,value):
    newNode = Node(value)
    newNode.next = head
    head = newNode

    return head


    
