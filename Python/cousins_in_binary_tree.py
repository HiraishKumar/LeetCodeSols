class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def replaceValueInTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return -1
        layer = [root]
        root.val = 0
        while layer:
            swap = []
            _sum = 0
            for node in layer:
                if node.left:
                    _sum += node.left.val
                    swap.append(node.left)
                if node.right:
                    _sum += node.right.val
                    swap.append(node.right)
            for node in layer:
                left_val = 0
                right_val = 0
                if node.left:
                    if node.right:
                        left_val = _sum - node.left.val - node.right.val
                    else:
                        left_val = _sum - node.left.val
                if node.right:
                    if node.left:
                        right_val = _sum - node.right.val - node.left.val
                    else:
                        right_val = _sum - node.right.val
                if node.left:
                    node.left.val = left_val
                if node.right:
                    node.right.val = right_val
            layer = swap
        return root