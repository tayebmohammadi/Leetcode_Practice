# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:


        def dfs(node, small, big):
            if not node:
                return True
            
            if node.val <= small or node.val >= big:
                return False
            
            return  dfs(node.left, small, node.val) and dfs(node.right, node.val, big)
        
        return dfs(root,  float("-inf"), float("inf"))


        































        
        # res = True
        # def dfs(node, left, right):
        #     nonlocal res

        #     if not node:
        #         return True

        #     if not (node.val > left and node.val < right):
        #         return False
        #     else:
        #         return (dfs(node.left, left, node.val) and
        #                 dfs(node.right, node.val, right))
        # return dfs(root, -math.inf, math.inf)

             
            
