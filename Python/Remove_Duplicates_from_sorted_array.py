class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        r = 0
        res = 1
        while r < len(nums)-1:
            if nums[r+1] != nums[r]:
                nums[res] = nums[r+1]
                res += 1 
            r+=1
        return res