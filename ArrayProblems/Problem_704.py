"""
704. Binary Search
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. 
If target exists, then return its index. Otherwise, return -1.
You must write an algorithm with O(log n) runtime complexity.
Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

"""
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        start = 0
        end = len(nums)-1
        while start<=end:
            mid = int((start + end)/2)
            if(target == nums[mid]):
                return mid
            elif(target>nums[mid]):
                start = mid+1
            else:
                end = mid-1
        return -1

nums = [-1,0,3,5,9,12]
target = 9
Solution().search(nums,target)

        