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
        front = head.next  ## head.next.next = head and also dont use newHead to reverse (cannot return the newHead atlast)
        front.next = head
        head.next = None
        return newHead
ll =  Linkedlist(1,2,3,4,5)
used_head = ll.head
solution = Solution()
reversed_head = solution.reverseList(used_head)
print(reversed_head.value)

# Iterative method:
class Solution:
    def reverseList(self, head):
        # l_list = head
        current_node = head
        previous_node = None
        next_node = None
        while current_node:
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node
            # l_list.head = previous_node
        return previous_node
    
ll =  Linkedlist(1,2,3,4,5)
used_head = ll.head
solution = Solution()
reversed_head = solution.reverseList(used_head)
print(reversed_head.value)