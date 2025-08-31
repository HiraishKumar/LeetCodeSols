class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def hasCycle(head:ListNode) -> bool:
    ''' Uses the floyd's hare and Tort algo for going through the list to find a cycle in the linked list'''
    fast=head
    slow=head
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
        if slow==fast:
            return True
    return False
    