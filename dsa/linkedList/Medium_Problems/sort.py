class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def merge(left,right):
    dummy = Node(0)
    temp = dummy

    while left is not None and right is not None:
        if left.data <= right.data:
            temp.next = left
            left = left.next

        else:
            temp.next = right
            right = right.next

        temp = temp.next

    if left is not None:
        temp.next = left

    else:
        temp.next = right

    return dummy.next

def sortLL(head):
    if head is None and head.next is None:
        return head
    
    slow = head
    fast = head.next

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    rightHead = slow.next
    slow.next = None

    left = sortLL(head)
    right = sortLL(rightHead)

    return merge(left,right)




