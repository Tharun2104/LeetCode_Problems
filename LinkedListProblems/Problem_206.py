# Definition for singly-linked list.
from LinkedList import Linkedlist
from LinkedList import LinkedNode

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        if (head is None or head.next is None):
            return head
        newHead = self.reverseList(head.next)
        front = head.next
        front.next = head
        head.next = None
        return newHead
ll =  Linkedlist(1,2,3,4,5)
used_head = ll.head
solution = Solution()
reversed_head = solution.reverseList(used_head)
print(reversed_head.value)