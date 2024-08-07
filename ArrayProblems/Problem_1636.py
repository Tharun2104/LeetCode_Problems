"""
https://leetcode.com/problems/sort-array-by-increasing-frequency/description/
"""
from typing import Counter, List


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        dt = dict(Counter(nums))
        k2 = dict((sorted(dt.items(), key = lambda ele: ele[0], reverse=True)))
        k3 = dict((sorted(k2.items(), key = lambda ele: ele[1])))
        res = []
        for i in k3:
            p = 1
            while p<=k3[i]:
                res.append(i)
                p+=1
        return res
    

# Method 2 
from collections import Counter

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        # Count the frequency of each number in the list using Counter
        num_frequency = Counter(nums)
      
        # Sort the numbers based on the frequency (ascending order)
        # When frequencies are the same, sort by the number itself (descending order)
        sorted_nums = sorted(nums, key=lambda x: (num_frequency[x], -x))
      
        return sorted_nums
                        