nums= [0,0,3,4]
target=0

def IndexFinder(nums:list[int],num:int)->int:
    left,right=0,len(nums)-1
    while right >= left :
        middle = (left+right) // 2  
        if nums[middle]==num:
            return middle 
        elif nums[middle] < num:
            left = middle + 1            
        else:
            right = middle - 1
            
    return -1       


# def twoSum(nums: list[int], target: int) -> list[int]:
#     results = []
#     for i in range(len(nums)):
#         num = target - nums[i]
#         left, right = i + 1, len(nums) - 1  

#         while left <= right:
#             middle = (left + right) // 2
#             if nums[middle] == num:
#                 results.append(i + 1)
#                 results.append(middle + 1)
#                 return results 
#             elif nums[middle] < num:
#                 left = middle + 1
#             else:
#                 right = middle - 1

#     return results  

# print(twoSum(nums,number))

def twosum(nums,target):
    results=[]
    for index,value in enumerate(nums):
        if target-value in nums:
            results.append(index+1)
            while nums.index(target-value)!=index and len(results)<2:
                results.append(nums.index(target-value)+1)
        break
    return results
print(twosum(nums,target))