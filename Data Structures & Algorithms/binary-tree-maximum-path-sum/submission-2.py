# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:


        longest = -math.inf

        def dfs(node):
            nonlocal longest

            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)

            longest = max(longest, node.val + left + right)
            return max(node.val + left, node.val + right, 0) 
        
        dfs(root)
        return longest




















        
        # res = -math.inf

        # def maxPath(node):
        #     nonlocal res

        #     if not node:
        #         return 0
            
        #     left_max = max(maxPath(node.left), 0)
        #     right_max = max(maxPath(node.right), 0)

        #     res = max(res, left_max + right_max + node.val)
        #     return node.val + max(left_max, right_max)

        # maxPath(root)
        # return res
    
            
            