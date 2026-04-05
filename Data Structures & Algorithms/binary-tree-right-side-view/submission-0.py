# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        res = []

        def dfs(root, height):
            nonlocal res
            if not root:
                return

            if height < len(res):
                res[height] = root.val
            else:
                res.append(root.val)
            
            
            dfs(root.left, height + 1)
            dfs(root.right,height + 1)

        dfs(root, 0)
        return res

            

        