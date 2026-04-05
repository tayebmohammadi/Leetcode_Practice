class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {}
        j = 0
        for i in nums:

            num = target - i
            if num in seen:
                return [seen[num], j]
            seen[i] = j
            j += 1
        