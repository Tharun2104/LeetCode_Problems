"""
442. Find All Duplicates in an Array
Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer 
appears once or twice, return an array of all the integers that appears twice.
You must write an algorithm that runs in O(n) time and uses only constant extra space.
Example 1:
Input: nums = [4,3,2,7,8,2,3,1]
Output: [2,3]

"""

nums = [4,3,2,7,8,2,3,1]
class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        result = []
        for ele in nums:
            if nums[abs(ele) - 1] < 0:
                result.append(abs(ele))
            else:        
                nums[abs(ele)-1] *= -1
        return result
        
Solution().findDuplicates(nums)

