from _heapq import heappop
"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def __init__(self) -> None:
        self.changes = {}

    def addMeetings(self, start, end):

        self.changes[start] = self.changes.get(start, 0) + 1
        self.changes[end] = self.changes.get(end, 0) - 1

        currRoom = 0
        maxRoom = 0

        for _, val in sorted(self.changes.items()):
            currRoom += val
            maxRoom = max(currRoom, maxRoom)
        return maxRoom

    def assignRooms(self, intervals):

        order = sorted(range(len(intervals)), 
            key= lambda i: intervals[i].start)
        
        rooms = [] # this is a heap for tracking the end times. it has (end, roomID)
        assigned = [0] * len(intervals)
        roomCount = 0
        
        for i in order:
            start = intervals[i].start
            end = intervals[i].end

            if rooms and rooms[0][0] <= start:
                _, roomID = heapq.heappop(rooms)
            else:
                roomID = roomCount
                roomCount += 1

            assigned[i] = roomID
            heapq.heappush(rooms, (end, roomID))
        return roomCount, assigned

        


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


            




