"""
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]):
        result = []
        queue = []
        if(root is None):
            return
        queue.append(root)
        zig = True
        while queue:
            curlvlsiz = len(queue)
            curlvlvls = []
            for _ in range(curlvlsiz):
                curvalue = queue.pop(0)
                if(zig):
                    curlvlvls.append(curvalue.val)
                else:
                    curlvlvls.insert(0,curvalue.val)
                if(curvalue.left):
                    queue.append(curvalue.left)
                if(curvalue.right):
                    queue.append(curvalue.right)
            result.append(curlvlvls)
            zig = not zig
        
        return result



        