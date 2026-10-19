# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root:
            return None

        
        self.invertTree(root.left)
        self.invertTree(root.right)

        root.left, root.right = root.right, root.left

        return root


























        # def invert(node):
        #     if not node:
        #         return None

        #     node.left, node.right = node.right, node.left

        #     invert(node.right)
        #     invert(node.left)
        # invert(root)
        # return root


        