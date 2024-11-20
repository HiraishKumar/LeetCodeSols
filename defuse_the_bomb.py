_code = [5,7,1,4]
_k = 3

def decrypt(code: list[int], k: int) -> list[int]:
    n = len(code)
    ans = [0]*n
    if k == 0:
        return ans
    
    if k > 0:
        count = sum(code[1:k+1])
        ans[0] = count
        for l in range(1,n):
            r = (l+k) % n
            count = count - code[l] + code[r]
            ans[l] = count
        return ans
    
    count = sum(code[-1:k-1:-1])
    ans[0] = count
    for l in range(1,n):
        r = (l-k) % n
        count = count - code[-l] + code[-r]
        ans[-l] = count
    return ans
    print(count)



print(decrypt(_code,_k))