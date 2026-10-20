# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # if not root:
        #     return []
        # res =[]
        # q = deque()

        # q.append(root)
        # while q:
        #     length = len(q)
        #     arr = []
        #     for _ in range(length):
                
        #         a = q.popleft()
        #         if a.left:
        #             q.append(a.left)
        #         if a.right:
        #             q.append(a.right)
        #         arr.append(a.val)
        #     res.append(arr)
        # return res


        res = []

        def dfs(node, height):
            if not node:
                return

            if len(res) == height:
                res.append([])

            res[height].append(node.val)

            dfs(node.left, height + 1)
            dfs(node.right, height + 1)
        dfs(root, 0)
        return res
        
            








        # res = []
        # def dfs(root, height):

        #     if not root:
        #         return 
            
        #     
        #    if height == len(res):
        #        res.append([])

        #    res[height].append(root.val)

        #     dfs(root.left, height + 1)
        #     dfs(root.right, height + 1)
        
        # dfs(root,0)

        # return res
            


        