"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted(intervals, key=lambda x: x.start)
        end = sorted(intervals, key=lambda x: x.end)

        maxRoom = 0
        currRoom = 0

        s, e = 0, 0 
        while s < len(start):
            if start[s].start < end[e].end:
                currRoom += 1
                maxRoom = max(maxRoom, currRoom)
                s += 1
            elif start[s].start >= end[e].end:
                currRoom -= 1
                e += 1
        return maxRoom





































        # start = sorted([i.start for i in intervals])
        # end = sorted([i.end for i in intervals])

        # room = 0
        # maxRoom = 0

        # s, e = 0, 0

        # while s < len(start):

        #     if start[s] < end[e]:
        #         room += 1
        #         s += 1
        #         maxRoom = max(room, maxRoom)
        #     elif start[s] >= end[e]: 
        #         room -= 1
        #         e += 1
            
        # return maxRoom


            




