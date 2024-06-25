"""
19.Remove Nth Node From End of List
Given the head of a linked list, remove the nth node from the end of the list and return its head.
Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

"""
# Approach - Before start iterating the slow pointer start iterating the fast pointer by n times
#            After that start iterating the slow pointer. Hence both pointers will be n spaces seperated. Once
#            the fast pointer reaches the end at that point slow pointer is at nth node from end update slow pointer
# TC - 0(N), SC - O(N)
#Code
from LinkedList import Linkedlist
from LinkedList import LinkedNode
class Solution:
    def removeNthFromEnd(self, head, n: int):
        dummy = LinkedNode(0)
        dummy.next = head
        fast = dummy
        slow = dummy
        for _ in range(n+1):
            fast = fast.next
        while fast:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next

ll =  Linkedlist(1,2,3,4,5)
used_head = ll.head
n = 2
solution = Solution()
solution.removeNthFromEnd(used_head,n)

