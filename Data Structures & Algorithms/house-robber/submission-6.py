class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2: 
            return max(nums)

        prev1, prev2 = nums[1], nums[0]

        for i in range(2, len(nums)):
            prev1, prev2 = nums[i] + prev2, max(prev1, prev2)
        return max(prev1, prev2)






























        # m = len(nums)

        # if m == 1:
        #     return nums[0]

        # if m == 2:
        #     return max([nums[0], nums[1]])

        # rob = []
        # rob.append(nums[0])
        # rob.append(max(nums[0], nums[1]))

        # for i in range(2,len(nums)):
        #     rob.append(max(nums[i] + rob[i - 2], rob[i - 1]))

        # return max(rob[-1], rob[-2])


        # rob1, rob2 = 0, 0 

        # for i in nums:
            
        #     temp = max(i + rob2, rob1)

        #     rob2 = rob1
        #     rob1 = temp 
            

        # return rob1
            