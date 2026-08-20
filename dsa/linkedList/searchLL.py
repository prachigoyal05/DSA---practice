class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def searchLL(head,key):
    temp = head

    while temp is not None:
        if temp.data == key:
            return True

        temp = temp.next

    return False
