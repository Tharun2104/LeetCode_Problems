# Sliding Window Median Problem

## Problem Statement
Given an array of integers `nums` and an integer `k`, there is a sliding window of size `k` which is moving from the very left of the array to the very right. You can only see the `k` numbers in the window. Each time the sliding window moves right by one position, you need to calculate the median of the current window in `O(log k)` time.

## Solution Explanation

### Max Heap and Min Heap
- **Max Heap**: Stores the smaller half of the numbers (as negative values to simulate max behavior using Python's min-heap).
- **Min Heap**: Stores the larger half of the numbers.
- **Purpose**: To quickly access the median, we need two heaps where the max heap stores the lower half and the min heap stores the upper half of the numbers.

### Balancing the Heaps
- Ensures the heaps remain balanced: the max heap can only be larger than the min heap by at most one element.
- **BalanceHeaps Function**: Moves elements between heaps to maintain this balance.

### Python's Heap Implementation
- Python's `heapq` library provides a min-heap. To simulate a max-heap, we store negative values.
  
### Removing Elements from Heaps
- **RemoveIndex Function**: Finds and removes an element from a heap while maintaining the heap property. It replaces the element with the last element in the heap and then re-heapifies the structure.

## Code
```python
class Solution:
    import heapq
    
    def __init__(self):  
        self.min_heap = []
        self.max_heap = []
        self.result = []

    def balanceHeaps(self):
        if len(self.max_heap) < len(self.min_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
        elif len(self.max_heap) > len(self.min_heap) + 1:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        
    def removeIndex(self, heap, removeNumber):
        idx = heap.index(removeNumber)
        last_node = heap[-1] 
        heap[idx] = last_node       
        del heap[-1]
        if idx < len(heap):
            if last_node > removeNumber:
                heapq._siftup(heap, idx)
            else:
                heapq._siftdown(heap, 0, idx)
        self.balanceHeaps()   

    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        for ind, num in enumerate(nums):
            # Insert
            if not self.max_heap or num <= -self.max_heap[0]:
                heapq.heappush(self.max_heap, -num)
            else:
                heapq.heappush(self.min_heap, num)
            
            self.balanceHeaps()
            
            if (ind+1) - k >= 0:
                if len(self.max_heap) == len(self.min_heap):
                    self.result.append((-self.max_heap[0] + self.min_heap[0]) / 2)
                else:
                    self.result.append(-self.max_heap[0] / 1.0)

                removeNumber = nums[ind+1-k]
                if removeNumber <= -self.max_heap[0]:
                    self.removeIndex(self.max_heap, -removeNumber)
                else:
                    self.removeIndex(self.min_heap, removeNumber)
                                                 
        return self.result
