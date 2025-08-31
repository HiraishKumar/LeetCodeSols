# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def recursor (root,current_max)->int:
            if root is None:
                return 0
            good_nodes = 0
            if root.val >= current_max:
                good_nodes = 1
                current_max = root.val
 
            return recursor(root.right,current_max) + recursor(root.left,current_max) + good_nodes
        return recursor(root,root.val)
            
        