class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1

            while l < r:
                curr = nums[i] + nums[l] + nums[r]
                if curr > 0:
                    r -= 1
                elif curr < 0: 
                    l += 1
                
                elif curr == 0:
                    res.append([nums[i], nums[l], nums[r]])

                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res
            
                    
            
                    

                
                    


            




























        # nums.sort()
        # result: List[List[int]] = []
        # n = len(nums)

        # for k in range(n-2):
        #     if k > 0 and nums[k] == nums[k-1]:
        #         continue
            
        #     if nums[k] > 0:
        #         break
    

        #     i , j = k + 1, n -1

        #     while i< j:
        #         s = nums[k] + nums[i] + nums[j]
        #         if s == 0:
        #             result.append([nums[k], nums[i], nums[j]])
        #             i += 1
        #             j -= 1
        #             while nums[i] == nums[i-1] and i < n -1:
        #                 i += 1
        #             while nums[j] == nums[j+1] and j > k:
        #                 j -= 1

        #         elif s > 0:
        #             j -=1
        #         else:
        #             i += 1
        

        # return result




        