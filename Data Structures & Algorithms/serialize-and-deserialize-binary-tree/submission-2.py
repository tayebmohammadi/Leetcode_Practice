# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:

        # if not root:
        #     return ''
        
        # q = deque([root])
        # result = []

        # while q:

        #     node = q.popleft()
        #     if node:
        #         result.append(str(node.val))
        #         q.append(node.left)
        #         q.append(node.right)
        #     else:
        #         result.append("N")
        # return ",".join(result)


        res = []

        def dfs(node):
            if not node:
                res.append("N")
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(res)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        # if not data:
        #     return None

        # values = data.split(',')
        # root = TreeNode(int(values[0]))
        # q = deque([root])

        # i = 1
        # while q:
        #     node = q.popleft()

        #     if values[i] != 'N':
        #         node.left = TreeNode(int(values[i]))
        #         q.append(node.left)
            
        #     if values[i + 1] != 'N':
        #         node.right = TreeNode(int(values[i + 1]))
        #         q.append(node.right)

        #     i += 2
        # return root



        values = data.split(',')
        self.i = 0
        def dfs():
            if values[self.i] == "N":
                self.i += 1
                return None

            node = TreeNode(int(values[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            print(node.val)
            return node

        return dfs()







        # vals = data.split(",")
        # self.i = 0

        # def dfs():
        #     if vals[self.i] == "N":
        #         self.i += 1
        #         return None
        #     node = TreeNode(int(vals[self.i]))
        #     self.i += 1
        #     node.left = dfs()
        #     node.right = dfs()
        #     return node
        # return dfs()

    


