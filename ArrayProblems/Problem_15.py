"""
15. 3Sum
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k,
and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Expliont<br>on: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

"""
# Approach : 3 pointer approach i, start and end, TC - O(N^2)
nums = [-1,0,1,2,-1,-4]
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        nums.sort()
        # target = 0
        combination = []
        for i in range(n-2):
            if(i>0 and nums[i] == nums[i-1]):
                # print(nums[i], nums[i-1])
                continue
            start = i+1
            end = n-1
            while end>start:
                x,y,z = nums[i], nums[start], nums[end]
                triplet = x+y+z
                if (triplet == 0):
                    combination.append([x,y,z])
                    start = start +1
                    while (nums[start-1] == nums[start]) and (start < end):
                        start = start +1
                elif(triplet>0):
                    end = end-1
                else:
                    start = start+1
        return combination

Solution().threeSum(nums)