import math
piles = [3,6,7,11]
h = 8

def minEatingSpeed(piles: list[int], h: int) -> int:    
    left=math.ceil(sum(piles)/h)
    right=max(piles)
    result=right
    while right >= left:
        fill=0
        middle=(left+right) // 2
        for i in piles:
            fill+=math.ceil(i / middle)
        if fill <= h:
            result=min(result,middle)
            right=middle-1
        else:
            left=middle+1
    return result 
    
print(minEatingSpeed(piles,h))