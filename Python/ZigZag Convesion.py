string="ABCD"
def convert(s:str,r:int):
    ans=""
    j=0
    leanth=len(s)
    test=(leanth//r)*(r+1)
    if r > 1:
        ans=s        
    while j<r-1:
        for i in range(0,leanth+test,2*(r-1)):
            if j>0:
                if 0 <= i-j < leanth:
                    ans+=s[i-j]
                if 0 <= i+j < leanth:
                    ans+=s[i+j]
            else:
                if 0 <= i < leanth:
                    ans+=s[i]
        j+=1
    for k in range(r-1,leanth,2*(r-1)):
        ans+=s[k]
    return ans

print(convert(string,3))
        
         