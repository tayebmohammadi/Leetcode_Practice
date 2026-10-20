# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []

        
        q = deque()
        q.append(root)
        res = []
        res.append(root.val)

        while q:
            q_len = len(q)
            rightMost = None

            for _ in range(q_len):
                node = q.popleft()

                if node.left:
                    q.append(node.left)
                    rightMost = node.left
                if node.right:
                    q.append(node.right)
                    rightMost = node.right

            if rightMost:
                res.append(rightMost.val)
        return res
            

                








        # res = []
        # def dfs(node, height):
        #     if not node:
        #         return
            
        #     if len(res) == height:
        #         res.append(node.val) 

        #     dfs(node.right, height + 1)
        #     dfs(node.left, height + 1)

        # dfs(root, 0)
        # return res

            



























        # res = []

        # def dfs(root, height):
        #     nonlocal res
        #     if not root:
        #         return

        #     if height < len(res):
        #         res[height] = root.val
        #     else:
        #         res.append(root.val)
            
            
        #     dfs(root.left, height + 1)
        #     dfs(root.right,height + 1)

        # dfs(root, 0)
        # return res

            

        