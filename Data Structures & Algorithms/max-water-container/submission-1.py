class Solution:
    def maxArea(self, heights: List[int]) -> int:

        i = 0
        j = len(heights) - 1
        max_v = 0
        while i < j:
            vol = (j-i) * min(heights[i], heights[j])
            max_v = max(vol, max_v)
            if heights[i] < heights[j]:
                i += 1
            else: 
                j -= 1
                
        
        return max_v
        