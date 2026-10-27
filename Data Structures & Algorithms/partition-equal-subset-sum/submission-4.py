class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        ## Brute Force
        # if sum(nums) % 2:
        #     return False
        
        # def dfs(i, total):
        #     if i >= len(nums) or total < 0:
        #         return False
        #     if total == 0:
        #         return True
            
        #     return dfs(i + 1, total - nums[i]) or dfs(i + 1, total)

        # return dfs(0, sum(nums)// 2)

        if sum(nums) % 2:
            return False
        dp = set()
        dp.add(0)

        target = sum(nums) // 2

        for num in nums:
            temp = set()
            for added in dp:
                temp.add(added)
                if (num + added) <= target:
                    temp.add(num + added) 
                if target in temp:
                    return True
            dp = temp
        return False




        
        






































        # if sum(nums) % 2:
        #     return False
        
        # target = sum(nums) // 2

        # DP = set()
        # DP.add(0)

        # for i in nums:
        #     tempDP = set()
        #     for j in DP:
        #         tempDP.add(j + i)
        #         tempDP.add(j)
        #         if target in tempDP:
        #             return True

        #     DP = tempDP

        # return False



                

                    





        