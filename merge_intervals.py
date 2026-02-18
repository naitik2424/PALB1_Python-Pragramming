# Merge Intervals

class Solution:
    def merge(self, intervals):
        intervals.sort()
        merged = [intervals[0]]

        for i in range(1, len(intervals)):
            last = merged[-1]
            curr = intervals[i]

            if curr[0] <= last[1]:
                last[1] = max(last[1], curr[1])
            else:
                merged.append(curr)

        return merged
