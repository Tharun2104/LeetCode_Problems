"""
16. 3Sum Closest
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.
Return the sum of the three integers.
You may assume that each input would have exactly one solution.
Example 1:
Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

"""
class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        # print(nums)
        res = [0]
        check = [float("inf")]
        for i in range(len(nums)):
            start = i+1
            end = len(nums)-1
            while end>start:
                actual_sum = nums[i]+nums[start]+nums[end]
                # print("actual_sum =", actual_sum)
                dif = actual_sum - target
                # print("dif =", dif)
                if (abs(dif)<=check[0]):
                    check[0] = abs(dif)
                    res[0] = actual_sum
                    # print( "check =", check)
                    # print(nums[i],nums[start],nums[end])
                if(actual_sum == target):
                    return actual_sum
                elif(actual_sum>target):
                    end = end -1
                elif(actual_sum<target):
                    start = start+1
        return res[0]

nums = [-1,2,1,-4]
target = 1
Solution().threeSumClosest(nums, target)