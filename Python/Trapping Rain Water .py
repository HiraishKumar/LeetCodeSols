height = [0,1,0,2,1,0,1,3,2,1,2,1]

def trap(height:list[int])->int:
    test=list(enumerate(height))
    n = len(height)
    left = 0
    right = n - 1
    leftmax = 0
    rightmax = 0
    res = 0
    while left < right:
        if height[left] < height[right]:
            if height[left] > leftmax:
                leftmax = height[left]
            else:
                res += leftmax - height[left]
            left += 1
        else:
            if height[right] > rightmax:
                rightmax = height[right]
            else:
                res += rightmax - height[right]
            right -= 1
    return res  
print(trap(height))
        
        