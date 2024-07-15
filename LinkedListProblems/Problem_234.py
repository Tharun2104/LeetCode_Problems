"""
https://leetcode.com/problems/palindrome-linked-list/description/
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional
from ListNodeCreation import ListNode


class Solution:
    def reverse(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
        return prev
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        new_head = self.reverse(slow)
        while new_head:
            if(new_head.val == head.val):
                new_head = new_head.next
                head = head.next
            else:
                return False
        return True

        