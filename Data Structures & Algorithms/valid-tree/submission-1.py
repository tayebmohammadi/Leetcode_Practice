class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if not n:
            return True

        
        adj = { i:[] for i in range(n)}
        for v1,v2 in edges:
            adj[v1].append(v2)
            adj[v2].append(v1)

        
        visitSet = set()
        def dfs(i, par):

            if i in visitSet:
                return False

            visitSet.add(i)
            for j in adj[i]:
                if j == par:
                    continue
                
                if not dfs(j, i):
                    return False

            return True
        
        return dfs(0, -1) and len(visitSet) == n














        # if len(edges) > n - 1:
        #     return False

        # tree = { i:[] for i in range(n)}
        # for v1, v2 in edges:
        #     tree[v1].append(v2)
        #     tree[v2].append(v1)

        # visitSet = set()
        # queue = collections.deque([0])
        # visitSet.add(0)

        # while queue:
        #     node = queue.popleft()

        #     for nei in tree[node]:
        #         if nei not in visitSet:
        #             queue.append(nei)
        #             visitSet.add(nei)
        
        # return len(visitSet) == n



            
            

            




        