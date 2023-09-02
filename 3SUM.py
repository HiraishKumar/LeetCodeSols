nums = [-2,0,1,1,2]
'''
[[-2,0,2],[-2,1,1]]
'''

def threeSum(nums: list[int]) -> list[list[int]]:
    nums.sort()
    s=set()
    for i in range(len(nums)):
        j=i+1
        k=len(nums)-1
        while j < k :
            target = nums[i] + nums[j] + nums[k]
            if target==0:                
                input=(nums[i],nums[j],nums[k])
                s.add(input)  
                j+=1

          
            elif target > 0:
                k-=1
            elif target < 0:
                j+=1
    return [list(i) for i in s]    
          
print(threeSum(nums))    
                
            
