class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s)!=len(goal) or (s+s).find(goal)==-1:
            return False
        return True