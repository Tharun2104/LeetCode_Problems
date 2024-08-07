"""
https://leetcode.com/problems/lucky-numbers-in-a-matrix/description/
"""
from typing import List

class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        row_nums = []
        col_nums = [float("-inf")]*len(matrix[0])
        for i in matrix:
            row_nums.append(min(i))
            for j in range(len(i)):
                if(i[j]>col_nums[j]):
                    col_nums[j]=i[j]
        res = []
        for k in range(len(row_nums)):
            for m in range(len(col_nums)):
                if(row_nums[k]==col_nums[m]):
                    res.append(row_nums[k])
        return res