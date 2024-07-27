"""
https://leetcode.com/problems/k-closest-points-to-origin/
"""
import heapq
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import math
        res = []
        for i in points:
            res.append(math.sqrt(i[0]**2+i[1]**2))

        max_heap = []
        for j in range(k):
            heapq.heappush(max_heap, (-res[j],points[j]))

        for i in range(k, len(res)):
            number = res[i]
            if -number>max_heap[0][0]:
                heapq.heappop(max_heap)
                heapq.heappush(max_heap, (-number,points[i]))
        # print(max_heap)
        out = []
        for i in max_heap:
            out.append(i[1])

        return out
        