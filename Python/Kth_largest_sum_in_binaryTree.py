class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return -1

        layer = [root]
        sums = []
        while layer:
            summation = 0
            swap = []
            for node in layer:
                summation += node.val
                if node.left:
                    swap.append(node.left)
                if node.right:
                    swap.append(node.right)
            sums.append(summation)
            layer = swap

        if k > len(sums):
            return -1

        sums_sorted = sorted(sums, reverse=True)  
        return sums_sorted[k - 1]