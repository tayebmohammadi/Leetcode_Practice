class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        biggest = 0
        for i in piles:
            biggest = max(biggest, i)
        
        left = 1
        right = biggest

        while left <= right:
            mid = (left + right) // 2

            hours = 0
            for i in piles:
                hours += (i + mid - 1) // mid
            if hours > h:
                left = mid + 1
            else:
                right = mid - 1
        return left




        