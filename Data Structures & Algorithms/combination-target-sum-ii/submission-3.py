class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []

        candidates.sort()

        res = []
        subset = []
        def dfs(i, total):
            if total == target:
                res.append(subset.copy())
                return
            if i >= len(candidates) or total > target:
                return
            subset.append(candidates[i])
            dfs(i + 1, candidates[i] + total)

            subset.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates [i + 1]:
                i += 1

            dfs(i + 1, total)
        dfs(0, 0)
        return res









































        # candidates.sort()

        # ans = []
        # def dfs(res, total, i):
        #     if total == target:
        #         ans.append(res.copy())
        #         return
        #     elif total > target or i >= len(candidates):
        #         return 

        #     res.append(candidates[i])
        #     dfs(res, total + candidates[i], i + 1)
        #     res.pop()

        #     while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
        #         i += 1
        #     dfs(res, total, i + 1)
        
        # dfs([], 0, 0)

        # return ans











        
        