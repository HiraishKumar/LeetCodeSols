import heapq
class Solution:
    def findScore(self, nums: list[int]) -> int:
        min_heap = [(nums[i],i) for i in range(len(nums))]
        heapq.heapify(min_heap)
        score = 0
        while min_heap:
            num , idx = heapq.heappop(min_heap)
            if nums[idx] != -1:
                score += num
                nums[idx] = -1
                if idx > 0 and nums[idx - 1] != -1:
                    nums[idx - 1] = -1
                if idx < (len(nums) - 1) and nums[idx + 1] != -1:
                    nums[idx + 1] = -1
        return score 
        