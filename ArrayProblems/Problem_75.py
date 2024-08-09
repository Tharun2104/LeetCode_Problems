"""
https://leetcode.com/problems/sort-colors/description/
"""

from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start = 0
        end = 1
        while (start < (len(nums)-1) or end < (len(nums)-1)):
            if(nums[start]>nums[end]):
                nums[start], nums[end] = nums[end], nums[start]
            if(nums[start]==0) or end == len(nums)-1:
                start +=1
                end = start +1
            else:
                end = end +1