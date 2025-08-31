import math
import heapq
class Solution:
    def pickGifts(self, gifts: list[int], k: int) -> int:
        heap = [-i for i in gifts]
        heapq.heapify(heap)

        for _ in range(k):
            larg = -heapq.heappop(heap)
            rem = math.floor(math.sqrt(larg))
            heapq.heappush(heap,-rem)
        
        return -sum(heap)
    