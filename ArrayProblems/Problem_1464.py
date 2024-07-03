"""
1464. Maximum Product of Two Elements in an Array
Given the array of integers nums, you will choose two different indices i and j of that array. 
Return the maximum value of (nums[i]-1)*(nums[j]-1).

Example 1:
Input: nums = [3,4,5,2]
Output: 12 
Explanation: If you choose the indices i=1 and j=2 (indexed from 0), you will get the maximum value, that is, 
(nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 = 12.

"""
nums = [1,5,4,5]
class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        first_max = second_max = float('-inf')
        for i in range(len(nums)):
            if nums[i] > first_max:
                second_max = first_max
                first_max = nums[i]
                # first_max_index = i
            elif second_max < nums[i]: # and first_max_index != i:
                second_max = nums[i]


        return (first_max-1)*(second_max-1)

Solution().maxProduct(nums)