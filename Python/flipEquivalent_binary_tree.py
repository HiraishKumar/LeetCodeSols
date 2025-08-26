class Solution:
    def flipEquiv(self, root1, root2):
        
        def checker(node_1, node_2):
            if not node_1 and not node_2:
                return True
            if not node_1 or not node_2 or node_1.val != node_2.val:
                return False
            return ((checker(node_1.left, node_2.left) or checker(node_1.left, node_2.right)) and
                    (checker(node_1.right, node_2.right) or checker(node_1.right, node_2.left)))
        
        return checker(root1, root2)


        