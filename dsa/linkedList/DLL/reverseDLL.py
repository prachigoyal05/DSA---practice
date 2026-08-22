class Node():
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

def reverseDll(head):
    temp = head

    while temp is not None:
        temp.prev,temp.next = temp.next,temp.prev
        head = temp
        temp = temp.prev

    return head