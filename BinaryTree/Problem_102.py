"""
https://leetcode.com/problems/binary-tree-level-order-traversal/description/
"""
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]):
        queue = []
        result = []
        queue.append(root)
        if(root is None):
            return result
        while queue:
            currentLevelSize = len(queue)
            currentLevelValues = []
            for _ in range(currentLevelSize):
                curvalue = queue.pop(0)
                currentLevelValues.append(curvalue.val)
                if(curvalue.left):
                    queue.append(curvalue.left)
                if (curvalue.right):
                    queue.append(curvalue.right)
            result.append(currentLevelValues)
        
        return result
            

        

        