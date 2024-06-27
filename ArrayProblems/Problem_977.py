"""
977. Squares of a Sorted Array
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100]
nums is sorted in non-decreasing order

"""
nums = [-4,-1,0,3,10]
# Three Pointer Approach
class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        start = 0   # Start Pointer
        end = len(nums)-1  # End Pointer
        res = [None]*len(nums)  # Resulting array
        res_point = len(nums)-1  # Resulting Pointer
        while end>=start:  # TIME COMPLEXITY : O(N)/ SPACE COMPLEXITY O(N)
            if(nums[start]**2 > nums[end]**2):
                res[res_point] = nums[start]**2
                res_point -= 1
                start +=1
            else:
                res[res_point] = nums[end]**2
                res_point -= 1
                end -=1
        return res

test = Solution()
test.sortedSquares(nums)