class Solution:
    def numMagicSquaresInside(self, grid: list[list[int]]) -> int:
        rowlen = len(grid)
        collen = len(grid[0])
        
        
        if (rowlen < 3 or collen < 3):
            return 0
        
        def ismagic(grid:list[list[int]],row:int,col:int):
            rowsum = [0 for i in range(3)]
            colsum = [0 for i in range(3)]
            nums = []    
            for row_index in range(row-1,row+2):
                for col_index in range(col-1,col+2):
                    num = grid[row_index][col_index]
                    if not 1 <= num <= 9:
                        return False
                    if num in nums:
                        return False
                    nums.append(num)
                    colsum[col_index - col + 1] += num
                    rowsum[row_index - row + 1] += num
                    
            for sum in rowsum:
                if sum != 15:
                    return False
            for sum in colsum:
                if sum != 15:
                    return False
            if grid[row-1][col-1] + grid[row+1][col+1] != 10:
                return False
            if grid[row-1][col+1] + grid[row+1][col-1] != 10:
                return False 
            return True
        count = 0
        
        for row in range(1,rowlen-1):
            for col in range(1,collen-1):
                if grid[row][col] == 5 and ismagic(grid,row,col):
                    count+=1
        return count
        