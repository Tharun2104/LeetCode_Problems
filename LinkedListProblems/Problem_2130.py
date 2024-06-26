"""
2130. Maximum Twin Sum of a Linked List
In a linked list of size n, where n is even, the ith node (0-indexed) of the linked list is known as the twin of the (n-1-i)th node, if 0 <= i <= (n / 2) - 1.
For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the twin of node 2. These are the only nodes with twins for n = 4.
The twin sum is defined as the sum of a node and its twin.
Given the head of a linked list with even length, return the maximum twin sum of the linked list.
Example:
Input: head = [5,4,2,1]
Output: 6
Explanation:
Nodes 0 and 1 are the twins of nodes 3 and 2, respectively. All have twin sum = 6.
There are no other nodes with twins in the linked list.
Thus, the maximum twin sum of the linked list is 6. 

"""
# Approach - Finding the mid element and reversing the remaining nodes after the mid element
# TC - 0(N), SC - O(1)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from LinkedList import Linkedlist


class Solution:
    def pairSum(self, head) -> int:
        max_val = 0
        first = head
        second = head.next
        while second.next:
            first = first.next
            second = second.next.next
        first=first.next
        prev = None
        while first:
            temp = first.next
            first.next = prev
            prev = first
            # print(prev)
            first = temp
        back_head = prev
        first = head
        while back_head:
            if((first.value+back_head.value)>max_val):
                max_val = (first.value+back_head.value)
            first = first.next
            back_head = back_head.next
        return max_val
    
ll =  Linkedlist(4,2,2,3)
used_head = ll.head
solution = Solution()
print(solution.pairSum(used_head))