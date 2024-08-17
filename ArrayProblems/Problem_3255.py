"""
https://leetcode.com/problems/find-the-power-of-k-size-subarrays-ii/description/
"""

from typing import List

class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        res = []
        if(k ==1):
            return nums
        count = 1
        for i in range(1,len(nums)):
            if( nums[i-1]+1 == nums[i]):
                count +=1
            else:
                count =1
            if(i+1>=k and count>=k):
                res.append(nums[i])
            elif(i+1>=k):
                res.append(-1)
        return res