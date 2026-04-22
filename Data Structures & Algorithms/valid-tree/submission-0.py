class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) > n - 1:
            return False

        tree = { i:[] for i in range(n)}
        for v1, v2 in edges:
            tree[v1].append(v2)
            tree[v2].append(v1)

        visitSet = set()
        queue = collections.deque([0])
        visitSet.add(0)

        while queue:
            node = queue.popleft()

            for nei in tree[node]:
                if nei not in visitSet:
                    queue.append(nei)
                    visitSet.add(nei)
        
        return len(visitSet) == n



            
            

            




        