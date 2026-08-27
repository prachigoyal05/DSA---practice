class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def lengthCycle(head):
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            count = 1
            temp = slow.next
            while temp != slow:
                count+=1
                temp = temp.next

            return count


    return 0