input = [1,2,3,10,4,2,3,5]
def findLengthOfShortestSubarray( arr: list[int]) -> int:
    n = len(arr)
    left = 0
    right = n-1

    while (left + 1) < n and arr[left] <= arr[left + 1]:
        left += 1

    if left == n-1:
        return 0
    
    while (right) > 0 and arr[right - 1] <= arr[right]:
        right -= 1

    result = min( right , n - left - 1)
    i,j = 0 , right 
    while i <= left and j < n:
        if arr[i]<= arr[j]:
            result = min (result,j-i-1)
            i += 1
        else:
            j += 1
    return result
print(findLengthOfShortestSubarray(input))

res = [1,2,3,2,3,5]