"""
https://leetcode.com/problems/balanced-binary-tree/description/
"""
# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        final = True
        def test1(root):
            nonlocal final   # nonloacl is a keyword used to modify the variable which is defined in the outer function
            if (root is None):
                return 0
            lh = test1(root.left)
            rh = test1(root.right)
            if abs(rh-lh)>1:
                final = False
            return max(lh,rh)+1 
        test1(root)
        return final
            
        