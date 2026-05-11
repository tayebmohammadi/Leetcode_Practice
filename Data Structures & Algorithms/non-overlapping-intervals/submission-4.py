class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(key = lambda x: x[1])

        count = 0
        curr = intervals[0]
        for i in range(1, len(intervals)):

            if curr[1] <= intervals[i][0]:
                curr = intervals[i]
            else:
                count += 1

        return count 



        