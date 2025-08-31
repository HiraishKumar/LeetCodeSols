nums = [-1,1,0,-3,3]
import math

def productExceptSelf( nums: list[int]) -> list[int]:
        prod = math.prod(filter(lambda x: x != 0, nums))
        
        if nums.count(0) > 1:
            return [0 for num in nums]
        if nums.count(0) == 1:
            return [prod if num == 0 else 0 for num in nums]
        return [prod // num for num in nums]
        
    
print(productExceptSelf(nums))