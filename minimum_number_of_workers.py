class Solution:
    def minWorkers(self, arr):
        n = len(arr)
        intervals = []

        for i in range(n):
            if arr[i] != -1:
                start = max(0, i - arr[i])
                end = min(n - 1, i + arr[i])
                intervals.append((start, end))

        intervals.sort()
        

        count = 0
        i = 0
        current_end = 0

        while current_end < n:
            farthest = current_end

            while i < len(intervals) and intervals[i][0] <= current_end:
                farthest = max(farthest, intervals[i][1] + 1)
                i += 1

            if farthest == current_end:
                return -1

            current_end = farthest
            count += 1

        return count