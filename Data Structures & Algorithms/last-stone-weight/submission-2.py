class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        heap = []

        for stone in stones:
            heapq.heappush(heap, -1 * stone)

        while heap:

            a = - 1 * heapq.heappop(heap)
            if not len(heap):
                return a
            b = - 1 * heapq.heappop(heap)

            res = abs(a - b)
            if res:
                heapq.heappush(heap, -1 * res) 
        return 0
            
