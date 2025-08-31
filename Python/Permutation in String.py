s1='adc'
s2='xfeghdcda'

def checkInclusion(s1: str, s2: str) -> bool:
    '''checks the prescence of a permution of s1 to be 
    within s2 and returns a coresponding boolean value '''   
    #making the initial primary_hash 
    primary_hash={chr(97 + i): 0 for i in range(26)}
    for i in s1:
        primary_hash[i]+=1
    #initialising pointers
    left=0
    right=len(s1)
    
    # making intial secendory_hash that will be chceked at each 
    # iterarion as the window slides towards the right
    secendory_hash={chr(97 + i): 0 for i in range(26)}     
    for j in range(right):
        secendory_hash[s2[j]]+=1
    
    # the window slides towards the right matching each
    # iteration of the secendory_hash with the primary_hash 
    for k in range(right,len(s2)+1):
        if primary_hash==secendory_hash:
            return True
        else:
            right=k
            secendory_hash[s2[right]]+=1        
            secendory_hash[s2[left]]-=1
            left+=1
    return False 
    
                
print(checkInclusion(s1,s2))
