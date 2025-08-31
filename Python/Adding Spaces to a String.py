class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans = ""
        left = 0
        for right in spaces:
            ans += s[left:right]
            ans += " "
            left = right
        ans += s[right:]
        return ans