# Find Largest Value in Each Tree Row

## Problem Statement
Find the largest value in each row of a binary tree.

### Breath First Search (BFS): 
**Breadth First Search (BFS)** is a graph traversal algorithm that explores all the vertices in a graph at the current depth before moving on to the vertices at the next depth level. It starts at a specified vertex and visits all its neighbors before moving on to the next level of neighbors.

## Key Concepts
- **Queue**: Used to perform a level-order traversal (BFS).
- **BFS (Breadth-First Search)**: Processes nodes level by level, which is ideal for finding the largest value at each level.

## Why Use a Queue?
- A queue allows us to process nodes in the order they appear in the tree.
- By enqueuing left and right children, we maintain the correct processing order for BFS.

## Why BFS Instead of DFS?
- BFS processes nodes level by level, making it easier to track the maximum value at each level.
- DFS would require additional logic to determine level boundaries.

## Finding the Max for Each Level
1. Initialize `currentLevelMax` to negative infinity.
2. Process each node in the current level.
3. Update `currentLevelMax` with the maximum value encountered.
4. After processing all nodes in the current level, add `currentLevelMax` to the result list.

## Code

```python
# Sample tree:
#        1
#       / \
#      3   2
#     / \   \
#    5   3   9
```

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        if root is None:
            return result

        queue = []
        queue.append(root)

        while queue:
            currentLevelSize = len(queue)
            currentLevelMax = float('-inf')

            for _ in range(currentLevelSize):
                currentNode = queue.pop(0)
                currentLevelMax = max(currentLevelMax, currentNode.val)

                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)

            result.append(currentLevelMax)

        return result

```




## Explanation

1. **Initialization**: We start by initializing an empty list `result` to store the maximum values.
2. **Edge Case**: If the tree is empty (`root` is `None`), we return an empty list.
3. **Queue Setup**: We initialize a queue and add the root node to it.
4. **BFS Loop**: We enter a loop that runs as long as there are nodes in the queue.
5. **Level Processing**:
   - We determine the number of nodes at the current level (`currentLevelSize`).
   - We initialize `currentLevelMax` to negative infinity.
   - We process each node in the current level, updating `currentLevelMax` with the maximum value encountered.
   - We add the left and right children of each node to the queue for the next level.
6. **Result Update**: After processing all nodes at the current level, we add `currentLevelMax` to the result list.
7. **Return Result**: Finally, we return the result list containing the largest values for each level.



