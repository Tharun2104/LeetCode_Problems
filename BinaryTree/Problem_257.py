"""
https://leetcode.com/problems/binary-tree-paths/description/
"""
from typing import List, Optional
# from BinaryTreeImplementation import TreeNode
from BinaryTreeImplementation import BinarySearchTree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root_node = TreeNode(1)
root_node.left = TreeNode(2)
root_node.right = TreeNode(3)
root_node.left.left = TreeNode(5)

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def binaryTreePathsUtils(node, curpath, allpaths):
            if node is None:
                return 
            curpath.append(str(node.val))
            if(node.left is None and node.right is None):
                allpaths.append("->".join(list(curpath)))
            else:
                binaryTreePathsUtils(node.left, curpath, allpaths)
                binaryTreePathsUtils(node.right, curpath, allpaths)
            curpath.pop()
            # return allpaths
        allpaths = []
        binaryTreePathsUtils(root, [], allpaths)
        return allpaths


Solution().binaryTreePaths(root_node)