# Merge Without Extra Space

import math

class Solution:
    def merge(self, a, b, n, m):
        gap = math.ceil((n + m) / 2)

        while gap > 0:
            i = 0
            j = gap

            while j < n + m:
                if i < n and j < n:
                    if a[i] > a[j]:
                        a[i], a[j] = a[j], a[i]
                elif i < n and j >= n:
                    if a[i] > b[j - n]:
                        a[i], b[j - n] = b[j - n], a[i]
                else:
                    if b[i - n] > b[j - n]:
                        b[i - n], b[j - n] = b[j - n], b[i - n]

                i += 1
                j += 1

            gap = 0 if gap == 1 else math.ceil(gap / 2)
