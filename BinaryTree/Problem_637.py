"""
https://leetcode.com/problems/average-of-levels-in-binary-tree/description/
"""
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]):
        result =[]
        queue = []
        if(root is None):
            return
        queue.append(root)
        while queue:
            size = len(queue)
            curlevelvalues = []
            for _ in range(size):
                curvalue = queue.pop(0)
                curlevelvalues.append(curvalue.val)
                if(curvalue.left):
                    queue.append(curvalue.left)
                if(curvalue.right):
                    queue.append(curvalue.right) 
            result.append(sum(curlevelvalues)/len(curlevelvalues))      
        return result