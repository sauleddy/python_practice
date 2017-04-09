# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if len(intervals) <= 1:
            return 0
        sorted(intervals, key=lambda interval: interval.start)
        result = 0
        idx_last = 0
        for idx in range(1, len(intervals)):
            if intervals[idx].start < intervals[idx_last].end:
                if intervals[idx].end < intervals[idx_last].end:
                    idx_last = idx
        return result
