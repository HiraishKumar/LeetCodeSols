s1='adc'
s2='dcda'

def checkInclusion(s1: str, s2: str) -> bool:
    hash={chr(97 + i): 0 for i in range(26)}
    test={chr(97 + i): 0 for i in range(26)} 
    for i in s1:
        hash[i]+=1
    left=0
    right=len(s1)
       
    for j in range(right):
        test[s2[j]]+=1
    for k in range(right,len(s2)):
        if hash==test:
            return True
        else:
            right=k
            test[s2[right]]+=1        
            test[s2[left]]-=1
            left+=1
    return hash == test   
    
                
print(checkInclusion(s1,s2))
