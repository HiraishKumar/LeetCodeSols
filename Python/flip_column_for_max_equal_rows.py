class Solution:
    def maxEqualRowsAfterFlips(self, matrix: list[list[int]]) -> int:
        dic = {}
        def ToString(arr:list)->str:
            res = ""
            if arr[0] == 0:
                for i in arr:
                    if i == 0:
                        res += "0"
                    else:
                        res += "1"
            else:
                for i in arr:
                    if i == 0:
                        res += "1" 
                    else:
                        res += "0"
            return res
        
        maximum = 0
        for row in matrix:
            row_str = ToString(row)
            if row_str not in dic:
                dic[row_str] = 1
                maximum = max(maximum, 1)
            else:
                dic[row_str] += 1
                maximum = max(maximum, dic[row_str])
        return maximum
