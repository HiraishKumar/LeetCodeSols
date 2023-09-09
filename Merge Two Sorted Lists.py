class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) ->ListNode:
        '''creates a 3rd list node (or linked list) and returns the pointer to the head of the 3rd list'''
        cur = dummy = ListNode()
        #duplicating pointers as the cur pointer by the end of the algorithm will be at the end of the linked list
        #dummy is place holder for the start (pointer) of the linked list
        while list1 and list2:               
            if list1.val < list2.val:
                cur.next = list1
                cur=list1
                list1=list1.next
            else:
                cur.next = list2
                cur =  list2
                list2=list2.next
        #if the two lists are of unequal leanth         
        if list1 or list2:
            cur.next = list1 if list1 else list2
        # we start with cur.ext=list1 dummp is one pointer behind the start of the list    
        return dummy.next
        