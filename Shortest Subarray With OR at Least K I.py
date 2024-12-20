class Solution:
    def minimumSubarrayLength(self, nums: list[int], k: int) -> int:
        n = len(nums)
        ans = float('inf')
        for i in range(n):
            val = 0 
            for j in range(i+1):
                val |= nums[j]

                if val >= k:
                    ans = min(ans,j-i+1) 

        return -1 if ans == float('inf') else ans