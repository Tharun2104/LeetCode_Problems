"""
189. Rotate Array
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
Example 1:
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

"""
# Approach: swaping elements, TC - O(N), SC - O(1)
class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k%n
        def reverse(start,end):
            while(start<end):
                nums[start], nums[end] = nums[end], nums[start]
                start, end =  start + 1, end -1
        
        # reverse(0,n-1)  # reversing whole list
        # reverse(0,k-1)  # reversing first k elements
        # reverse(k,n-1)  # reversing last n-k elements
        # Another way
        reverse(0,(n-k-1))  # reversing first n-k elements
        reverse((n-k),n-1)  # reversing last k elements
        reverse(0,n-1)      # reversing whole list
        return nums
nums = [1,2,3,4,5,6,7]
k = 3
Solution().rotate(nums,k)

# Approach 2 : slicing
class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums)
        nums[:] = nums[-k:]+nums[:-k]
        return nums
nums = [1,2,3,4,5,6,7]
k = 3
Solution().rotate(nums,k)