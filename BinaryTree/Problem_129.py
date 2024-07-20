"""
https://leetcode.com/problems/sum-root-to-leaf-numbers/description/
"""
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        value = 0
        res = []
        def test(root, cur, value, res):
            if(root is None):
                return
            cur.append(root)
            value = value*10 + root.val
            if(root.left is None and root.right is None):
                res.append(value)
                print(res)
                return root.val
            test(root.left, cur, value, res)
            test(root.right, cur, value, res)
            cur.pop()
            return sum(res)
        return test(root, [], value,res)

        