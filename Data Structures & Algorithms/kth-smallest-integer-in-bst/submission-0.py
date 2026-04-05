# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = 0

        def smallest(node):
            nonlocal res, k

            if k < 0:
                return 0

            if not node:
                return 

            smallest(node.left)
            k -= 1
            if k == 0:
                res = node.val
            smallest(node.right)

        smallest(root)

        return res

            
            
            
        