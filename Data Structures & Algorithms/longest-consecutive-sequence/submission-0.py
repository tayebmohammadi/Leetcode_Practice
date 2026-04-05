class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0

        s = set(nums)
        best = 0
        for x in s:

            if (x-1) not in s:
                y = x + 1
                length = 1
                while y in s:
                    length += 1
                    y += 1
                best = max(length, best)
        return best







        

        