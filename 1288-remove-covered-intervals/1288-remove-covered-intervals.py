class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        count=len(intervals)
        intervals.sort(key=lambda x:(x[0], -x[1]))
        maxEnd=intervals[0][1]
        for st, end in intervals[1:]:
            if end<=maxEnd:
                count-=1
            else:
                maxEnd=end
        return count