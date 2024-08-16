"""
https://leetcode.com/problems/permutations/
"""

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        # base case
        if(len(nums)==1):
            return [nums[:]]
        
        for i in range(len(nums)):
            n = nums.pop(0)

            prems = self.permute(nums)

            for i in prems:
                i.append(n)
            
            res.extend(prems)
            nums.append(n)
        return res
