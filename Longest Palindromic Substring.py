test='caaaaa'
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
'''explanation??????
def longestPalindrome(self, s):
        longest_palindrom = ''
        dp = [[0]*len(s) for _ in range(len(s))]
        #filling out the diagonal by 1
        for i in range(len(s)):
            dp[i][i] = True
            longest_palindrom = s[i]
			
        # filling the dp table
        for i in range(len(s)-1,-1,-1):
				# j starts from the i location : to only work on the upper side of the diagonal 
            for j in range(i+1,len(s)):  
                if s[i] == s[j]:  #if the chars mathces
                    # if len slicied sub_string is just one letter if the characters are equal, we can say they are palindomr dp[i][j] =True 
                    #if the slicied sub_string is longer than 1, then we should check if the inner string is also palindrom (check dp[i+1][j-1] is True)
                    if j-i ==1 or dp[i+1][j-1] is True:
                        dp[i][j] = True
                        # we also need to keep track of the maximum palindrom sequence 
                        if len(longest_palindrom) < len(s[i:j+1]):
                            longest_palindrom = s[i:j+1]
                
        return longest_palindrom
'''

print(longestPalindrome(test)) 