import heapq

nums = [1,1,1,1,1,1,1,1,12,21,3,3,3,3]
k = 2

from collections import Counter
# def topKFrequent(nums:list[int],k:int)->list:
#     dic={}
#     lst=[]
#     for i in nums:
#         if i in dic:
#             dic[i] = dic[i] + 1
#         else:
#             dic[i] = 1
            
#     alpha=sorted(dic.items(), key=lambda item: item[1])  
#     for j in range(1,k+1):
#         lst.append(alpha[-j][0])
        
#     return lst
    



def topKFrequent( nums: list[int], k: int) -> list[int]:
    count = Counter(nums)
    heap = []
    for key in count:
        heapq.heappush(heap, [count[key], key])
        if len(heap) > k:
            heapq.heappop(heap)
        
    res = []
    while heap:
        res.append(heapq.heappop(heap)[1])
    return res
print(topKFrequent(nums,k))