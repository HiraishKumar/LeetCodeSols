array1 = [1,2,3,0,0,0]
array2 = [2,5,6] 

def merge( nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    cnt1 = 0
    cnt2 = 0
    cnt = 0
    
    while cnt1 < m and cnt2 < n:
        
        if nums1[cnt] > nums2[cnt2]:
            for i in range(m + n - 1, cnt, -1):
                nums1[i] = nums1[i - 1]
            nums1[cnt] = nums2[cnt2]

            cnt2 += 1
            cnt += 1
        else:
            cnt1 += 1
            cnt += 1
    
    while cnt2 < n:
        
        for i in range(m + n - 1, cnt, -1):
            nums1[i] = nums1[i - 1]
        nums1[cnt] = nums2[cnt2]
        cnt2 += 1
        cnt += 1
merge(array1,3,array2,3)
print(array1)        