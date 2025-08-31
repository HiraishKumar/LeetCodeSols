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