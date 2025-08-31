from collections import defaultdict
s = "AABABBA"
k = 2
def characterReplacement( s: str, k: int) -> int:
    r =j = 0
    d = defaultdict(int)
    for i, a in enumerate(s):
        d[a]+=1
        if d[a] > r:r = d[a]
        elif i - j + 1 > r + k:
            d[s[j]]-=1
            j+=1
    return min(r + k, len(s))
    # start=0
    # end=0
    # margin=k
    # maxi=0
    # for i in range(1,len(s)):
    #     if s[i] == s[start]:
    #         end=i            
    #     elif s[i] != s[start] and margin > 0:
    #         end=i
    #         margin-=1
    #     else:
    #         maxi=max(end-start+1,maxi)
    #         start = i            
    #         margin=k            
    # return max(end-start+1,maxi)

print(characterReplacement(s,k))