from _heapq import heapify
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-i for i in stones]
        heapq.heapify(stones)

        while stones:

            a = - 1 * heapq.heappop(stones)
            if not stones:
                return a
            b = - 1 * heapq.heappop(stones)

            res = abs(a - b)
            if res:
                heapq.heappush(stones, -1 * res) 
        return 0
            
