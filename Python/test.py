_banned = [11]
_n = 7
_maxSum = 50

def maxCount( banned: list[int], n: int, maxSum: int) -> int:
    curr = 0
    crossed = 0
    test = set(banned)

    for i in range(1,n+1):
        if (curr + i > maxSum):
            break
        elif i not in test:
            curr += i
            crossed += 1
    return crossed 

print(maxCount(_banned,_n,_maxSum))
