class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        preMap = { i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        state = [0] * numCourses
        res = []

        ## 0 = unvisited, 1 = visiting, 2 = processed
        def dfs(crs):
            if state[crs] == 1:
                return False
            if state[crs] == 2:
                return True
            
            state[crs] = 1

            for pre in preMap[crs]:
                if not dfs(pre):
                    return False

            state[crs] = 2
            res.append(crs)
            return True

        for crs in range(numCourses):
            if state[crs] == 0:
                if not dfs(crs):
                    return []

        return res


        