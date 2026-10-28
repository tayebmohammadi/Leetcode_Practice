import heapq
from collections import defaultdict, deque
from typing import List
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        freq = defaultdict(int)
        for c in tasks:
            freq[c] += 1

        heap = [[-val, key] for key, val in freq.items()]
        heapq.heapify(heap)

        q = deque()
        time = 0

        while q or heap:
            time += 1
            
            while q and q[0][1] <= time:
                task, availableTime = q.popleft()
                heapq.heappush(heap, task)
            
            if heap:
                task = heapq.heappop(heap)
                task[0] += 1

                if task[0] < 0:
                    q.append([task, time + n + 1])
            
        return time

            
            
















































        # count = Counter(tasks)

        # most = max(count.values())
        # most_freq = list(count.values()).count(most)

        # ans = (most - 1) * (n + 1) + most_freq

        # return max(len(tasks), ans)




        