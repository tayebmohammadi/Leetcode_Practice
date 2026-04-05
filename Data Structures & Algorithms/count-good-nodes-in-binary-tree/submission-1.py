# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        res = 0


        def dfs(root, biggest):
            nonlocal res

            if not root:
                return
            
            if root.val >= biggest:
                res += 1
                biggest = root.val
            dfs(root.left, biggest)
            dfs(root.right, biggest)

        dfs(root,-math.inf)

        return res

