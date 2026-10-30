class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums:
            return []

        res = []
        subset = []
        def dfs(i, total):
            if total == target:
                res.append(subset.copy())
                return
            if total > target or i >= len(nums):
                return

            subset.append(nums[i])
            dfs(i, nums[i] + total)
            subset.pop()
            dfs(i + 1, total)
            
        dfs(0, 0)
        return res



            







































        # res = []
        # subset = []
        # tot = 0

        # def dfs(tot, i):

        #     if i >= len(nums) or tot > target:
        #         return 

        #     if tot == target:
        #         res.append(subset.copy())
        #         return
            
        #     subset.append(nums[i])
        #     dfs(tot + nums[i], i)
        #     subset.pop()
        #     dfs(tot, i + 1)
   
        # dfs(tot, 0)

        # return res
 