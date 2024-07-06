"""
162. Find Peak Element
A peak element is an element that is strictly greater than its neighbors.
Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.
You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.
You must write an algorithm that runs in O(log n) time.

Example:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.

"""
nums = [1,2,3,1]
class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        start = 0
        end = len(nums)-1
        while (end>start):
            mid = (start + end )//2
            if(nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]):
                return mid
            elif(nums[mid]<nums[mid+1]):
                start = mid +1
            else:
                end = mid
        return start

Solution().findPeakElement(nums)  

