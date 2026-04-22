class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        adj = { i:[] for i in range(n)}
        for v1,v2 in edges:
            adj[v1].append(v2)
            adj[v2].append(v1)

        visited = set()
        count = 0

        def dfs(node):
            visited.add(node)

            for nei in adj[node]:
                if nei not in visited:
                    dfs(nei)

            
        for node in range(n):
            if node not in visited:
                dfs(node)
                count += 1
            

        return count