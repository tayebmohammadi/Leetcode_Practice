# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        res = True
        def dfs(node, left, right):
            nonlocal res

            if not node:
                return True

            if not (node.val > left and node.val < right):
                return False
            else:
                return (dfs(node.left, left, node.val) and dfs(node.right, node.val, right))
        return dfs(root, -math.inf, math.inf)

             
            
