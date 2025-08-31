nums = [4,5,6,7,0,1,2]
target=0
# nums=[0, 1, 2, 4, 5, 6, 7]
def search(nums:list[int],target:int)->int:
    n = len(nums)
    l = 0
    r = n-1
    while l<=r:
        m = l+(r-l)//2
        if nums[m]==target:
            return m
        if nums[m]>=nums[l]:
            if target>=nums[l] and target<nums[m]:
                r = m - 1
            else:
                l = m + 1
        else:  
        # if nums[m]<nums[l]:
            if target<=nums[r] and target>nums[m]:
                l = m + 1
            else:
                r = m - 1
    return -1


    # right=0
    # if target not in nums:
    #     return -1
    # if nums[0]!=min(nums):
    #     while nums[right] > nums[right-1]:
    #         right-=1
    # nums=nums[right:]+nums[:right]
    # l,r=0,len(nums)-1
    # middle=0
    # while l<=r:
    #     middle=(l+r)//2
    #     if nums[middle]==target:
    #         result=middle+right
    #         if result > -1:
    #             return result
    #         else:
    #             return len(nums)+result
            
    #     elif nums[middle] > target:
    #         r=middle-1
    #     elif nums[middle] < target:
    #         l=middle+1
    # return -1

print(search(nums,target))
     


    
