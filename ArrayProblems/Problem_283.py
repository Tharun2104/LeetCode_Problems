"""
283. Move Zeroes
Example 1:
Input: nums= [0,1,0,3,12]
Output: [1,3,12,0,0]

"""
nums= [0,1,0,3,12]
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        last_zero_index = 0 # is initialized to 0. 
        # This variable keeps track of the position where the next non-zero element should be moved to.

        for index, num in enumerate(nums): #O(N)
            if num != 0: # swap
                nums[last_zero_index], nums[index] = nums[index], nums[last_zero_index]
                last_zero_index += 1
            # print(last_zero_index)
            # print(nums)
    
        return nums
test = Solution()
test.moveZeroes(nums)