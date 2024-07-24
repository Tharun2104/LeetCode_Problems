"""
https://leetcode.com/problems/find-largest-value-in-each-tree-row/description/
"""
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]):
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
            result.append(max(curlevelvalues))      
        return result  