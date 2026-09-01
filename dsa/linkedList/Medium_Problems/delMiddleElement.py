class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def delMiddle(head):

    if head is None or head.next is None:
        return None
    
    prev = None
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        prev = slow
        fast = fast.next.next
        slow = slow.next

    prev.next = slow.next

    return head