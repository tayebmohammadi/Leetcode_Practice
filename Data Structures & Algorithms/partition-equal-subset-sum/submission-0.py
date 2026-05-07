class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        
        target = sum(nums) // 2

        DP = set()
        DP.add(0)

        for i in nums:
            tempDP = set()
            for j in DP:
                tempDP.add(j + i)
                tempDP.add(j)
                if target in tempDP:
                    return True

            DP = tempDP

        return False



                

                    





        