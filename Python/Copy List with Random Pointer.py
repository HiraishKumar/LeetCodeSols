class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: '[Node]') -> '[Node]':
        '''we make 2 passes initially we make the same number of
        objects as in the intial list and arrange them in corespondece 
        in a hash map, and on the second pass we connect thier next 
        and random pointers '''
        pointer_map={None:None}
        curr=head
        while curr:
            copy=Node(curr.val)
            pointer_map[curr]=copy
            curr=curr.next
        curr=head
        while curr:
            copy=pointer_map[curr]
            copy.next=pointer_map[curr.next]
            copy.random=pointer_map[curr.random]
            curr=curr.next

        return pointer_map[head]
        