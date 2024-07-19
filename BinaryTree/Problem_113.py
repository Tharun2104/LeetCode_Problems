"""
https://leetcode.com/problems/path-sum-ii/
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSumUtill(self, root, CurPath, MatPath,target):
        if(root is None):
            return
        CurPath.append(root.val)
        value = root.val
        if(value == target and root.left is None and root.right is None):
            MatPath.append(list(CurPath))
        else:
            self.pathSumUtill(root.left, CurPath, MatPath, target-root.val)
            self.pathSumUtill(root.right, CurPath, MatPath, target-root.val)
        CurPath.pop()
        return MatPath
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> list[list[int]]:
        CurPath = []
        MatPath = []
        return self.pathSumUtill(root, CurPath, MatPath, targetSum)