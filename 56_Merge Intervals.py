# 时间：20190510
# Exampole1:
# Input: [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
# Example2:
# Input: [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
# 难度：Medium(0.5)

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        l = len(intervals)
        if l == 0:
            return res

        intervals = sorted(intervals)
        for i in range(l - 1):
            if intervals[i][1] < intervals[i + 1][0]:
                res = res + [intervals[i]]
            else:
                intervals[i + 1] = [intervals[i][0], max(intervals[i][1], intervals[i + 1][1])]
        res = res + [intervals[-1]]
        return res