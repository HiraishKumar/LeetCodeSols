_code = [5,7,1,4]
_k = 3

def decrypt(code: list[int], k: int) -> list[int]:
    n=len(code)
    ans=[0]*n
    if k==0: return ans
    if k>0:
        ans[0]=wsum=sum(code[1:k+1])
        for l in range(1, n):
            r=(l+k)%n
            wsum+=-code[l]+code[r]
            ans[l]=wsum
        return ans

    ans[0]=wsum=sum(code[-1:k-1:-1])
    for l in range(1, n):
        r=(l-k)%n
        wsum+=-code[-l]+code[-r]
        ans[-l]=wsum
    return ans


print(decrypt(_code,_k))