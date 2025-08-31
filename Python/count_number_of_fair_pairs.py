
from bisect import bisect_left, bisect_right

class Solution:
    def countFairPairs(self, v, lower, upper):
        v.sort()
        ans = 0
        for i in range(len(v) - 1):
            low = bisect_left(v, lower - v[i], i + 1)
            up = bisect_right(v, upper - v[i], i + 1)
            ans += up - low
        return ans






# _nums = [0,1,7,4,4,5]
# _test =[0, 1, 3, 4, 4, 5,6,7,8,9]
# _lower = 3
# _upper = 6
# def countFairPairs( nums: list[int], lower: int, upper: int) -> int:

#     nums.sort()
#     print(nums)

#     res= 0

#     l_l,r_l,l_r,r_r = 0,0,len(nums),len(nums)
#     l_mid,r_mid = 0,0 
#     if nums[0] <= lower:
#         while 0 <= l_mid < len(nums):
#             l_mid = (l_l + l_r) // 2
#             if nums[l_mid] <= lower < nums[l_mid+1]:
#                 l_mid += 1
#                 break
#             elif nums[l_mid] < lower:
#                 l_l = l_mid
#             elif nums[l_mid] > lower:
#                 l_r = l_mid
#     else:
#         l_mid = 0

#     if nums[-1] >= upper:
#         while 0 <= r_mid < len(nums):
#             r_mid = (r_l + r_r) // 2
#             if nums[r_mid-1] < upper <= nums[r_mid]:
#                 r_mid +=1 
#                 break
#             elif nums[r_mid] < upper:
#                 r_l = r_mid
#             elif nums[r_mid] > upper:
#                 r_r = r_mid
#     else:
#         r_mid = len(nums)-1


#     for i in range(l_mid,r_mid):
#         for j in range(l_mid,r_mid):
#             if j != i and (lower <= nums[i] + nums[j] <= upper):
#                 res+=1
                
#     print([l_mid,r_mid])
#     return res



# print(countFairPairs(_test,_lower,_upper))