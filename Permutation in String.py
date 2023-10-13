s1='ab'
s2='eidboaoo'

def checkInclusion(s1: str, s2: str) -> bool:
    left=0
    right=0
    for i in range(len(s2)):
        if s2[i] in s1:
            test=[i for i in s1] 
            left=i
            right=i 
            test.remove(s2[i])          
            while left <= right:                
                if not test:
                    return True
                elif left > 0 and (s2[left-1] in test):
                    left-=1
                    test.remove(s2[left]) 
                elif right < len(s2)-1 and (s2[right+1] in test):
                    right+=1
                    test.remove(s2[right])
                else:
                    break
    return False                 
                
print(checkInclusion(s1,s2))
