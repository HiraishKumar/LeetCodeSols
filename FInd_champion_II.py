class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        StrongerThan = [1]*(n)
        for index , pointer in edges:
            StrongerThan[pointer] = 0 
            
        champion = -1
        championCount = 0
        
        for team in range(n):
            if StrongerThan[team] == 1:
                champion = team
                championCount += 1
                
        if championCount == 1:
            return champion
            
        return -1    
        