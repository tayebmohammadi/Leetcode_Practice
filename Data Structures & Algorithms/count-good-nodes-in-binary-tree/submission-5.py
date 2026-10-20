# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        def dfs(node, biggest):
            if not node:
                return 0
            
            res = 1 if node.val >= biggest else 0
            biggest = max(biggest, node.val)

            return res + dfs(node.left, biggest) + dfs(node.right, biggest)

        return dfs(root, root.val)
         

            






























        # def dfs(root, biggest):

        #     if not root:
        #         return 0
            
        #     res = 1 if root.val >= biggest else 0

        #     biggest = max(biggest, root.val)
        #     res += dfs(root.left, biggest)
        #     res += dfs(root.right, biggest)

        #     return res
            
        # return dfs(root, root.val)

