n=2

def countbits(n:int)->list[int]:
    result=[]
    for i in range(n+1):
        test=format(i,'b')
        result.append(test.count('1'))
    return result
def countBits_alt(self, n: int) -> list[int]:
    res = [0] * (n + 1)
    for i in range(1, n + 1):
        if i % 2 == 1:
            res[i] = res[i - 1] + 1
        else:
            res[i] = res[i // 2]
    return res
        

print(countbits(n))