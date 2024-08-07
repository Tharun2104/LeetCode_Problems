"""
https://leetcode.com/problems/path-sum/description/
"""
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if(root is None):
            return
        if(root.val== targetSum and root.left is None and root.right is None):
            return True
        return self.hasPathSum(root.left,targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)
        
