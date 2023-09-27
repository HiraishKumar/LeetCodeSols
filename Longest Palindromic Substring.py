test='abcda'
def longestPalindrome(s: str) -> str:
    front=0
    back=0
    maxi=''   
    if len(s)==1 or len(s)==0 or s==s[::-1]:
        return s
    if len(s)==len(set(s)):
        return s[0]
    for i in range(len(s)-1):    
        if s[i]==s[i+1]:            
            back=i                
            front=i+1
            while front < len(s)-1 and back > 0 and s[front+1]==s[back-1]:
                back-=1
                front+=1  
                back_s=s[back]
                front_s=s[front]                          
            if len(maxi) < len(s[back:front+1]):
                maxi=s[back:front+1]
            else:
                pass                  
        elif i>0 and s[i-1] == s[i+1]:
            back=i-1
            front=i+1
            while front < len(s)-1 and back > 0 and s[front+1]==s[back-1]:
                back-=1
                front+=1 
                back_s=s[back]
                front_s=s[front]                                                     
            if len(maxi) < len(s[back:front+1]):
                maxi=s[back:front+1]
            else:
                pass   
    return maxi


print(longestPalindrome(test)) 