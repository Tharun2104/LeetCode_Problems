"""
https://leetcode.com/problems/binary-tree-inorder-traversal/
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List, Optional


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        respath = []   
#recursive solution below
        # def util(root, respath):
        #     if(root is None):
        #         return
        #     util(root.left, respath)
        #     respath.append(root.val)
        #     util(root.right, respath)
        #     return respath
        # return util(root,[])
#Iterative solution below
        curpath = []
        while root or curpath:
            while root:
                curpath.append(root)
                root = root.left
            
            root = curpath.pop()
            respath.append(root.val)
            root = root.right
        return respath
        




        