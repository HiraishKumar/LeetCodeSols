class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}  # map key to node

        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    # remove node from list
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    # insert node at right
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            # remove from the list and delete the LRU from hashmap
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
    
    
obj=LRUCache(2)
print(obj.put(1,1))
print(obj.put(2,2))
print(obj.get(1))
print(obj.put(3,3))
print(obj.get(2))
print(obj.put(4,4))
print(obj.get(1))
print(obj.get(3))
print(obj.get(4))


# class Node:
#     def __init__(self, key, value):
#         self.key = key
#         self.value = value
#         self.next = None
# class LRUCache:
#     def __init__(self, capacity: int):
#         self.capacity=capacity
#         self.head=None       
#         self.load=0  
#     def remove_end(self)->Node:
#         head=self.head
#         if head.next is None:
#             return
#         while head.next.next is not None:
#             head=head.next
#         head.next=None
#         return head   

#     def get(self, key: int) -> int:
#         poin=self.head
#         if self.head.key==key:
#             return self.head.value
#         while poin.next is not None:
#             if poin.key==key:
#                 prev.next=poin.next
#                 temp=self.head
#                 self.head=poin
#                 poin.next=temp                
#                 return poin.value
#             prev=poin
#             poin=poin.next
#         return -1

#     def put(self, key: int, value: int) -> None:
#         if self.load==0:
#             self.head=Node(key,value)
#             self.load+=1
#             return
#         if self.load==self.capacity:
#             end=self.remove_end()
#             end.next=Node(key,value)
#             return
#         poin=self.head
#         while poin.next is not None:
#             poin=poin.next
#         poin.next=Node(key,value)
#         self.load+=1
#         return 

