"""
92. Reverse Linked List II
Given the head of a singly linked list and two integers left and right where left <= right, 
reverse the nodes of the list from position left to position right, and return the reversed list
Example:
Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]

"""
# Approach - Iterating to the left and reversing the sublist
# TC - O(1), SC - O(1)
# Approach 1:
from ListNodeCreation import ListNode


class Solution:
    def reverseBetween(self, head, left: int, right: int):
        dummy = ListNode(0,head)
        prev  = dummy
        index = 1
        cur = head
        while cur:
            if(index == left):
                temp = None
                r_tail = cur
                while(index <= right):
                    temp2 = cur.next
                    cur.next = temp
                    temp = cur
                    cur = temp2
                    index+=1
                r_tail.next = cur
                prev.next = temp
                return dummy.next
            prev = cur
            cur = cur.next
            index+=1

# Approach 2: used for loop
class Solution:
    def reverseBetween(self, head, left: int, right: int):
        dummy = ListNode(0, head)

        # 1) reach node at position "left"
        leftPrev, cur = dummy, head
        for i in range(left - 1):
            leftPrev, cur = cur, cur.next

        # Now cur="left", leftPrev="node before left"
        # 2) reverse from left to right
        prev = None
        for i in range(right - left + 1):
            tmpNext = cur.next
            cur.next = prev
            prev, cur = cur, tmpNext

        # 3) Update pointers
        leftPrev.next.next = cur  # cur is node after "right"
        leftPrev.next = prev  # prev is "right"
        return dummy.next