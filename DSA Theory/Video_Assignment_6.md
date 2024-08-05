# Cheat Sheet for Top 'K' Numbers

## Heap : 
A heap is a specialized tree-based data structure that satisfies the heap property. Heaps are commonly used to implement priority queues and to perform heap sort. There are two primary types of heaps: min-heaps and max-heaps.

## Problem Description

Given a list of numbers and an integer `K`, find the top `K` largest numbers from the list.

### Example
```python
nums = [11, 15, 29, 2, 3, 16]
K = 3

import heapq

def top_k_numbers(nums, k):
    min_heap = []
    
    for i in range(k):
        heapq.heappush(min_heap, nums[i])
        
    for i in range(k, len(nums)):
        number = nums[i] 
        if number > min_heap[0]:
            heapq.heappop(min_heap)
            heapq.heappush(min_heap, number)
            
    return min_heap

print(top_k_numbers(nums, K))
```
## Explanation of Top 'K' Numbers Using Min-Heap

### 1. Why Load Up K Elements into a Heap?

- **Heap Type**: We use a **min-heap** for this problem. In a min-heap, the smallest element is always at the root. This property is useful because we only need to maintain the top `K` largest elements, and the smallest of these `K` elements will always be the root.

- **Initial Loading**: We first load the first `K` elements into the min-heap to initialize it. This ensures our heap contains `K` elements, and the root of the heap represents the smallest element among these `K` elements.

### 2. Updating the Heap for K-N Elements

- **Process**: For each new element beyond the first `K` elements, compare it with the smallest element in the min-heap (the root).

- **Condition**: If the new number is greater than the smallest element in the heap, we replace the smallest element:
  - **Remove** the smallest element using `heapq.heappop()`.
  - **Add** the new number using `heapq.heappush()`.

- **Reason**: This process ensures that the heap always contains the top `K` largest numbers from the list. The smallest of these `K` numbers is always the root, and any number greater than this root should be added to the heap, while the smallest number is removed.

### 3. How Does a Heap Help Solve This Problem?

- **Efficiency**: A heap allows us to efficiently maintain a subset of `K` largest elements with operations that are logarithmic in complexity. Adding and removing elements from a heap are `O(log K)` operations, making this approach efficient for large lists.

- **Space Complexity**: The space complexity is `O(K)`, as we only need to store `K` elements in the heap.


### Visual Representation
```python
Input : nums = [11, 15, 29, 2, 3, 16], K = 3

# First For loop itertation :

Step 1: Heap: [11]

   11

Step 2: Heap: [11, 15]

     11
       \
        15
    
Step 3: Heap: [11, 15, 29]

     11
    /  \
   15   29



### Second for loop:

# Adding 2
Heap: [11, 15, 29]

     11
    /  \
   15   29


#Adding 3
Heap: [11, 15, 29]

     11
    / \
   15  29

#Adding 16 - Replaces 11 from the heap 
Heap: [11, 29, 15]  - [29, 15, 16]

     15
    /  \
   16   29
```



