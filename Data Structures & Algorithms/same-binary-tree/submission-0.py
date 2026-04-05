# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if not p and not q:
            return True
        
        
        res = True


        def dfs(r1,r2):
            nonlocal res
            if not r1 and not r2:
                return
            elif not r1 or not r2:
                res = False
                return

            l = r1.val
            r = r2.val
            if r != l:
                res = False

            dfs(r1.left, r2.left)
            dfs(r1.right, r2.right)

        dfs(p,q)
        return res


             

        