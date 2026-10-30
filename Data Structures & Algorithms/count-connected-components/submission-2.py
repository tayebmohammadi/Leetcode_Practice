class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if not edges:
            return 0

        graph = defaultdict(list)

        for v1, v2 in edges:
            graph[v1].append(v2)
            graph[v2].append(v1)
        
        visited = set()
        def dfs(node): ## explore the connested part and mark them as visited
            if node in visited:
                return
            
            visited.add(node)

            for nei in graph[node]:
                dfs(nei)
        count = 0
        for node in graph.keys():
            if node not in visited:
                dfs(node)
                count += 1
        return count + n - len(visited)


        







































        # adj = { i:[] for i in range(n)}
        # for v1,v2 in edges:
        #     adj[v1].append(v2)
        #     adj[v2].append(v1)

        # visited = set()
        # count = 0

        # def dfs(node):
        #     visited.add(node)

        #     for nei in adj[node]:
        #         if nei not in visited:
        #             dfs(nei)

            
        # for node in range(n):
        #     if node not in visited:
        #         dfs(node)
        #         count += 1
            

        # return count