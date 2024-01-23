array1 = [2, 3, 5, 7, 9]
array2 = [1, 2, 4, 6]

def merge( nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    p1,p2=0,0
    n+=1
    m+=1
    nums1.append(float('inf'))
    nums2.append(float('inf'))
    res=[]
    while p1<m and p2<n:
        if nums1[p1]>nums2[p2]:
            res.append(nums2[p2])
            if p1+1<m and p2+1<n and (nums1[p1+1] >= nums2[p2+1] >= nums1[p1]):
                p2+=1
            else:
                p1+=1   
        elif nums1[p1]<nums2[p2]:
            res.append(nums1[p1])
            if p1+1<m and p2+1<n and (nums2[p2+1] >= nums1[p1+1] >= nums2[p2]):
                p1+=1
            else:
                p2+=1
        else:
            res.append(nums2[p2])
            res.append(nums1[p1])
            p1+=1
            p2+=1 
    return res        
print(merge(array1,5,array2,4))        