arr = [3,2,3,2,3,2]
sub_len = 2

def resultsArray( nums: list[int], k: int) -> list[int]:
    res = []
    l=0
    isValid = 1
    if k == 1:
        return nums 
    for r in range(1, len(nums)):
        if nums[r - 1] + 1 == nums[r]:
            isValid += 1
        if r - l + 1 > k:
            if nums[l] + 1 == nums[l + 1]:
                isValid -= 1
            l += 1  
        if r - l + 1 == k:
            res.append(nums[r] if isValid == k else -1)
    return res
        

print(resultsArray(arr,sub_len))