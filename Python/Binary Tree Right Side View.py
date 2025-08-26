class Solution:
    def rightSideView(self, root ) -> list[int]:
        def dfs(origin,deapth):
            if origin is not None:
                if len(result)==deapth:
                    result.append(origin.val)
                dfs(origin.right,deapth+1)
                dfs(origin.left,deapth+1)
        result =[]
        dfs(root,0)
        return result
        