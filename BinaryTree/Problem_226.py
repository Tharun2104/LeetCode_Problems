"""
https://leetcode.com/problems/invert-binary-tree/description/
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def test(root):
            if( root is None):
                return
            temp = root.left
            root.left = root.right
            root.right = temp
            test(root.left) or test(root.right)
            return
        test(root)
        return root
        