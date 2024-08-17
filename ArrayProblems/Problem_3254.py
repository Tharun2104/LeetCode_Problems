"""
https://leetcode.com/problems/find-the-power-of-k-size-subarrays-i/
"""
from typing import List

#Brute Force
class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        res = []
        for i in range(len(nums)):
            start = i
            end = i+k-1
            if(end < len(nums)):
                while start < end:
                    if(nums[start]+1 ==nums[start+1]):
                        start = start+1
                    else:
                        # print(nums[start])
                        res.append(-1)
                        break
                # print(nums[start])
                if(start == end):
                    res.append(nums[end])
        return res


# optimised
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