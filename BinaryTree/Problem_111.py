"""
https://leetcode.com/problems/minimum-depth-of-binary-tree/description/
"""
# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if (root is None):
            return 0
        queue = []
        count = 0
        queue.append(root)
        while queue:
            size = len(queue)
            count +=1
            for _ in range(size):
                curvalue = queue.pop(0)
                if(curvalue.left is None and curvalue.right is None):
                    return count
                if(curvalue.left):
                    queue.append(curvalue.left)
                if(curvalue.right):
                    queue.append(curvalue.right)
            

                
            


        