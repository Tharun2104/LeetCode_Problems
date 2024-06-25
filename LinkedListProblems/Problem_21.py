"""
21. Merge Two Sorted Lists
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.
Example:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

"""
# Approach - Interchange the node connections by verifying min of each node
# TC - O(N), SC - O(1)

from LinkedList import LinkedNode


class Solution:
    def mergeTwoLists(self, list1, list2):
        dummy_head = tail = LinkedNode()
        L1 = list1
        L2 = list2
        while L1 and L2:
            if(L1.val < L2.val):
                tail.next = L1
                L1 = L1.next
            else:
                tail.next = L2
                L2 = L2.next
            tail = tail.next
        tail.next = L1 or L2
        return dummy_head.next