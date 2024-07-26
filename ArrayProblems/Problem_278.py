"""
https://leetcode.com/problems/first-bad-version/
"""
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        start = 1
        end = n
        if(isBadVersion(start)): # type: ignore
            return start
        while(start<=end):
            mid = (start+end)//2
            if(isBadVersion(mid)): # type: ignore
                end = mid - 1
            else:
                start = mid +1
        return start
        
