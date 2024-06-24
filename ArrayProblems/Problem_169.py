"""
169. Majority Element:
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array
Example 1:
Input: nums = [3,2,3]
Follow-up: Could you solve the problem in linear time and in O(1) space?
Output: 3

"""
# nums = [3,2,3]
# nums = [6,5,5]
# Boyer-Moore Voting Algorithm: Brief explanation below
"""
Candidate Selection Phase:
    Start with no fruit as the current favorite (candidate) and a score of zero.
    Walk around the party and for each person you ask:
        If your score is zero, take note of the fruit they like as your current candidate.
        If the person likes the same fruit as your current candidate, increase your score by one.
        If the person likes a different fruit, decrease your score by one.

"""
nums = [3,3,4]
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        vote = 0
        candidate = 0
        for i in nums:  #O(N)
            if(vote == 0):
                candidate = i
            if(i == candidate):
                vote += 1
            else:
                vote -= 1
            # print(vote)
        return candidate
    
test = Solution()
test.majorityElement(nums) 
