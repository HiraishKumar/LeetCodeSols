class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def can_distribute(x):
            count = 0
            for q in quantities:
                count += math.ceil(q/x)
            return count <= n
        l = 1
        r = max(quantities)
        res = 0
        while l <= r:
            mid = (l+r)//2
            if can_distribute(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res 
        