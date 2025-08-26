class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummyHead = ListNode()
        tail = dummyHead
        carry = 0

        while l1 is not None or l2 is not None or carry != 0:
            digit1 = l1.val if l1 is not None else 0
            digit2 = l2.val if l2 is not None else 0

            sum = digit1 + digit2 + carry
            digit = sum % 10
            carry = sum // 10

            newNode = ListNode(digit)
            tail.next = newNode
            tail = tail.next

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

        result = dummyHead.next
        dummyHead.next = None
        return result
    def MultiplyTwoNumbers(self,l1:ListNode,l2:ListNode)->ListNode:
        dummyHead=ListNode(0)
        tail=dummyHead
        carry=0
        while l1 is not None or l2 is not None or carry != 0:
            digit1 = l1.val if l1 is not None else 0
            digit2 = l2.val if l2 is not None else 0
            
            prod = ( digit1 * digit2 ) + carry
            digit = prod % 10
            carry = prod // 10
            
            NewNode=ListNode(digit)
            tail.next=NewNode
            tail=tail.next
            
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
            
        result=dummyHead.next
        dummyHead.next=None
        return result
    
    def InRange(self,_range:int)->ListNode:
        dummyHead = ListNode()
        tail = dummyHead
        
        for i in range(1,_range+1):
            newNode=ListNode(i)
            tail.next=newNode
            tail=tail.next
        result = dummyHead.next
        dummyHead.next = None
        return result        
    
    
    
l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))

t1 = ListNode(5)
t2 = ListNode(2)

solution = Solution()

result1 = solution.addTwoNumbers(l1, l2)
result2 = solution.InRange(5)
result3 = solution.MultiplyTwoNumbers(t1, t2)

while result1 is not None:
    print(result1.val,end='')
    result1=result1.next

print('\n') 

while result2 is not None:
    print(result2.val,end='')
    result2=result2.next

print('\n') 

while result3 is not None:
    print(result3.val,end='')
    result3=result3.next