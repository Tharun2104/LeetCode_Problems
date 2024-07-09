"""
53. Maximum Subarray
Given an integer array nums, find the subarray with the largest sum, and return its sum.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

"""
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        cur_sum = 0
        max_sum = float("-inf")
        for i in nums:
            cur_sum = cur_sum + i
            max_sum = max(max_sum, cur_sum)
            if(cur_sum < 0):
                cur_sum = 0
        return max_sum
        
    
nums = [-2,1,-3,4,-1,2,1,-5,4]
Solution().maxSubArray(nums)