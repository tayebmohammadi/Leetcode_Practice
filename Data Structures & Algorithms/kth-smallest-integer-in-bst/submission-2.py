# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        res = 0
        stack = []
        curr = root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            
            curr = stack.pop()
            res += 1
            if res == k:
                return curr.val
            curr = curr.right












        
        # res = 0
        # def dfs(node):
        #     nonlocal res, k
        #     if not node: 
        #         return
            
        #     dfs(node.left)
        #     k -= 1

        #     if k == 0:
        #         res = node.val
        #         return
        #     dfs(node.right)
            
        # dfs(root)
        # return res

        # res = 0

        # def smallest(node):
        #     nonlocal res, k

        #     if k < 0 or not node:
        #         return 

        #     smallest(node.left)
        #     k -= 1
        #     if k == 0:
        #         res = node.val
        #         return 
        #     smallest(node.right)

        # smallest(root)

        # return res


     