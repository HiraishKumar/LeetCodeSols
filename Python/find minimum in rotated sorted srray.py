nums=[3,4,5,1,2]

def findMin(nums: list[int]) -> int:
    if nums[0] <= nums[-1]:
        return nums[0]
    l, r = 0, len(nums) - 1
    while l <= r: 
        mid = (l + r) // 2
        if nums[mid + 1] <= nums[mid]:
            return nums[mid + 1]
        elif nums[l] <= nums[mid]:
            l = mid + 1
        else: 
            r = mid - 1
    return nums[0]
print(findMin(nums))