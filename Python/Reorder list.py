class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def reorderList(head: [ListNode]) -> None:
    """
    Do not return anything, modify head in-place instead.
    """
    #finding middle
    slow,fast=head,head.next
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
    #reversing second half
    second=slow.next
    prev=slow.next=None
    while second:
        temp=second.next
        second.next=prev
        prev=second
        second=temp
    first, second= head, prev
    # merging first and second half
    while second:
        temp1,temp2=first.next,second.next
        first.next=second
        second.next=temp1
        first,second=temp1,temp2

