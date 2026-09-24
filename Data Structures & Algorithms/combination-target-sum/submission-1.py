class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []
        tot = 0
        subset = []
        def dfs(i, tot):
            
            
            if i >= len(nums):
                return 
            if tot == target:
                res.append(subset.copy())
                return
            if tot > target:
                return 

            tot += nums[i]
            subset.append(nums[i])
            dfs(i, tot)

            tot -= nums[i]
            subset.pop()
            dfs(i + 1, tot)

        dfs(0, tot)
        return res







































        # result = []

        # def dfs(i, cur, total):
        #     if total == target:
        #         result.append(cur.copy())
        #         return
        #     if i >= len(nums) or total > target:
        #         return

        #     cur.append(nums[i])
        #     dfs(i, cur, total + nums[i])

        #     cur.pop()
        #     dfs(i + 1, cur, total)
        
        # dfs(0, [], 0)

        # return result

        


                

            

            

            






        