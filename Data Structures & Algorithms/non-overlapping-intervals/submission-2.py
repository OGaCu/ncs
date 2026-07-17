class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort by start
        # compare adjacent pairs
        # if overlap, delete the larger end value out of the overlapping
        # keep track of end
        # greedy select to leave greatest room
        intervals.sort()

        erase = 0
        currend = intervals[0][1]
        for i in range(1, len(intervals)):
            if currend > intervals[i][0]:
                # overlap
                erase += 1
                currend = min(intervals[i][1], currend)
            else:
                currend = intervals[i][1]
        return erase            

