class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)

        most = max(count.values())
        most_freq = list(count.values()).count(most)

        ans = (most - 1) * (n + 1) + most_freq

        return max(len(tasks), ans)




        