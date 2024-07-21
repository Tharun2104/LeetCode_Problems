"""
https://leetcode.com/problems/binary-tree-level-order-traversal-ii/description/
"""
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]):
        queue = []
        result = []
        if(root is None):
            return result
        queue.append(root)
        while queue:
            currentlevelsize = len(queue)
            currentlevelvalues = []
            for _ in range(currentlevelsize):
                curvalue = queue.pop(0)
                currentlevelvalues.append(curvalue.val)
                if(curvalue.left):
                    queue.append(curvalue.left)
                if(curvalue.right):
                    queue.append(curvalue.right)
            result.insert(0, currentlevelvalues)
        return result
        