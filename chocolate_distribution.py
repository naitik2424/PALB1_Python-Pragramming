# Chocolate Distribution Problem

class Solution:
    def findMinDiff(self, arr, m):
        arr.sort()
        n = len(arr)
        min_diff = float('inf')

        for i in range(n - m + 1):
            min_diff = min(min_diff, arr[i + m - 1] - arr[i])

        return min_diff
