"""
35. Search Insert Position
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:
Input: nums = [1,3,5,6], target = 7
Output: 4

"""
class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        start = 0
        end = len(nums)-1
        while(end>=start):
            mid = int(start + (end-start)/2)
            if(nums[mid]==target):
                return mid
            elif(nums[mid]<target):
                start = mid +1
            else:
                end = mid -1
        # print(start,mid, end)
        return start

nums = [1,3,5,6]
target = 7
        
Solution().searchInsert(nums,target)