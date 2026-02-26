class Solution:
    def findMedian(self, arr):
        arr.sort()
        n = len(arr)
        
        if n % 2 == 0:
            median = (arr[n//2] + arr[n//2 - 1]) / 2
        else:
            median = arr[n//2]
            
        return median